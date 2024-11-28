import logging


# Setup logging
logger = logging.getLogger()
logger.setlevel(logging.INFO)


class Middleware:

    def __init__(self, token: str, secret:str):
        self.token = str
        self.secret = secret

    def authorizeUser(self) -> str:
        try:
        decoded_token = jwt.decode(self.token, self.secret, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            logger.error("JWT token is expired. User is not authorized")
            return None
        except jwt.JWTClaimsError:
            logger.error("JWT claims and invalid. User is not authorized")
            return None
        except jst.JWTError:
            logger.error("Invalid JWT token. User is not authorized")
            return None
        except Exception as e:
            logger.error(f"An unexpected error as occured: {e}")
            return None

        return decoded_token