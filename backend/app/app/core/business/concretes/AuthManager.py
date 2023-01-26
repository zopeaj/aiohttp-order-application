from app.core.business.abstract.UserService import UserService
from app.core.business.abstract.EmailSenderService import EmailSenderService
from app.core.business.abstract.ConfirmationTokenService import ConfirmationTokenService
from app.core.business.abstract.RoleService import RoleService

class AuthManager:
    def __init__(self, userService, emailSenderService, confirmationTokenService, roleService):
        self.userService = userService
        self.emailSenderService = emailSenderService
        self.confirmationTokenService = confirmationTokenService
        self.roleService = roleService

    def register(user: UserDto) -> Result:
        pass

    def confirm(role: str) -> Result:
        pass

