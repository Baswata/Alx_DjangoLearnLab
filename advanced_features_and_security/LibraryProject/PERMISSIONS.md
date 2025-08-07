## Permissions and Groups

### Custom Permissions on `Article` model
- can_view
- can_create
- can_edit
- can_delete

### Groups
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: All permissions

### How it works
- Permissions are enforced in views using `@permission_required`
- Users are added to groups through the Django admin
