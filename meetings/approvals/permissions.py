from guardian.shortcuts import assign_perm, remove_perm


def add_approval_permissions_to_submission_contributor(approval, submission_contributor):
	assign_perm("approvals.delete_approval", submission_contributor, approval)


def remove_approval_permissions_to_submission_contributor(approval, submission_contributor):
	remove_perm("approvals.delete_approval", submission_contributor, approval)


def add_approval_permissions_to_conference_admin(approval, conference_admin):
	assign_perm("approvals.change_approval", conference_admin, approval)
	assign_perm("approvals.delete_approval", conference_admin, approval)

def remove_approval_permissions_to_conference_admin(approval, conference_admin):
	remove_perm("approvals.change_approval", conference_admin, approval)
	remove_perm("approvals.delete_approval", conference_admin, approval)
