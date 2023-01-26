from aiohttp.web import RouteTableDef, Response
from app.core.abstract.UserService import UserService
from app.schemas.user.user_add import UserCreate
from app.schemas.user.user_delete import UserDelete
from app.schemas.user.user_retrieve import UserData
from app.schemas.user.user_update import UserUpdate
from fastapi import jsonable_encoder

userrouter = RouteTableDef()

class UserController:
    authManager: AuthManager = AuthManager(userService, emailSenderService, confirmationTokenService)
    userService: UserService = UserService()

    @userrouter.get("/user/{id}")
    def getUser(request, id) -> UserData:
        user_id = request.get_param("userid")
        user = self.userService.getUserById(user_id)
        user_data = UserData(**user)
        if user:
            return Response(body=user_data, status=200)
        return Response(body={"detail": "user not found"}, status=204)

    @userrouter.post("/user/")
    def postUser(request) -> UserCreate:
        user = request.json()
        isSuccess = self.authManager.register(user)
        if isSuccess:
            return Response(body={"detail": "User Register Successfully, We just send a confirmation link to your email"}, status=200, text="Confirmation link is sent to your email")
        return Response(body={"detail": "Error while trying to register user"}, status=400)

    @userrouter.put("/user/{id}")
    def updateUser(request, id) -> UserUpdate:
        user_id = request.get_param("userid")
        user = request.json()
        user_instance_data = jsonable_encoder(user)
        if user_instance_data:
            user = self.userService.getUserById(user_id)
            if user is not None:
                user = self.userService.updateUser(user_id, user_instance_data)
                return Response(body=user, status=202, text="User Update Successfully")
        return Response(body={"detail":"User not updated"}, status=404)

    @userrouter.delete("/user/{id}")
    def deleteUser(request, id) -> UserDelete:
        user_id = request.get_param("userid")
        user = self.userService.findUserById(user_id)
        if user:
            self.userService.delete(user_id, user)
            return Response(body={"detail": "User deleted Successfully"}, status=404)
        return Response(body={"detail": "Error while trying to delete user"}, status=323)




