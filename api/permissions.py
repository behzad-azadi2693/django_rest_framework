from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    message = 'you must be the of this object'
    my_safe_method = ["GET","PUT"] #this just into double cotaitions
    
    def has_permission(self, request, view):#permisins for access to view
        if request.method in self.my_safe_method:
            return True
        return False

    def has_object_permission(self, request, view, obj):#permission for change object in view
        if request.method in SAFE_METHODS:
            return True # Check permissions for read-only request            
        return obj.user == request.user  # Check permissions for write request


class IsOwnerOrReadOnlyComment(BasePermission):
    message = 'you must be the of this object'
    def has_object_permission(self, request, view, obj):#permission for change object in view
        if request.method in SAFE_METHODS:
            return True # Check permissions for read-only request            
        return obj.user == request.user  # Check permissions for write request
