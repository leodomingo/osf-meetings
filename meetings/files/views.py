from django.shortcuts import render

# Create your views here.

class FileView(APIView):
    base_url = '{}oauth2/{}'.format(OsfOauth2AdapterConfig.osf_accounts_url, '{}')
    access_token_url = base_url.format('token')
    authorize_url = base_url.format('authorize')
    profile_url = '{}v2/users/me/'.format(OsfOauth2AdapterConfig.osf_api_url)
    node_url = '{}v2/nodes/'.format(OsfOauth2AdapterConfig.osf_api_url)
    print(node_url)

    def post(self, request, **kwargs):
        if request.user.is_authenticated():
            current_user = request.user.username
            account = Social.Account.objects.get(uid=current_user)
            osf_token = SocialToken.objects.get(account=account)
#            current_user_nodes_url = 
#            requests.post(self.

