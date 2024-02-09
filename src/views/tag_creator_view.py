from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.controllers.tag_creator_controller import TagCreatorController


class TagCreatorView:
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product-code"]

        # criação das tags
        tag_creation_controller = TagCreatorController()
        response = tag_creation_controller.create(product_code)
        #retorno http
        return HttpResponse(status_code=200, body=response)