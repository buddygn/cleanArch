from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface

class UserFinderControler(ControllerInterface):
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__user_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params['first_name']

        response = self.__user_case.find(first_name=first_name)

        return HttpResponse(
            status_code=200,
            body={'data': response}
        )
