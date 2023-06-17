from rest_framework.views import Request, Response, status


class Methods:
    def update_keys(keys, pet):
        for key, value in keys:
            if key != id:
                setattr(pet, key, value)


class ResponseMethods:
    def response_success(status_code, params="Params Success method"):
        match status_code:
            case 200:
                status_code = status.HTTP_200_OK
            case 201:
                status_code = status.HTTP_201_CREATED
            case 204:
                status_code = status.HTTP_204_NO_CONTENT
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(params, status_code)

    def response_error(status_code, params="Params Error method"):
        match status_code:
            case 400:
                status_code = status.HTTP_400_BAD_REQUEST
            case 403:
                status_code = status.HTTP_403_FORBIDDEN
        return Response(params, status_code)
