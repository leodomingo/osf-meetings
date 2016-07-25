from django.http import HttpResponse
from mail.mails import (SubmissionSuccessEmail,
                        SubmissionConfDNE, SubmissionWithoutFiles)
from conferences.models import Conference


def on_incoming_message(request):
    if request.method == 'POST':
        name_and_sender = request.POST.get('from')
        name = name_and_sender[:name_and_sender.index('<')].strip()  # noqa
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject', '')  # noqa

        body_plain = request.POST.get('body-plain', '')  # noqa
        body_without_quotes = request.POST.get('stripped-text', '')  # noqa
        # note: other MIME headers are also posted here...

        # attachments:
        files = []
        for key in request.FILES:
            file = request.FILES[key]
            # do something with the file
            files.append(file)

        conf_identifier = recipient.replace(
            '-poster@osf.io', "").replace('-talk@osf.io', "").strip()

        msg = ''
        # get/create user
        try:
            conf = Conference.objects.get(id=conf_identifier)
            if not files:
                raise ValueError('No file attachments')
        except Conference.DoesNotExist:
            msg = SubmissionConfDNE(to=sender,
                                    from_email=recipient)
        except ValueError:
            msg = SubmissionWithoutFiles(to=sender,
                                         from_email=recipient)
        else:
            # post submission here
            msg = SubmissionSuccessEmail(to=sender,
                                         from_email=recipient,
                                         conference=conf)
        finally:
            print(str(msg))
            # msg.send()

    # Returned text is ignored but HTTP status code matters:
    # Mailgun wants to see 2xx, otherwise it will make another attempt in 5
    # minutes
    return HttpResponse('OK')
