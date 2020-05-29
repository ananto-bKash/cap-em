from service.limit_service import LimitService
from service.config_service import ConfigService
from db.base import Session


session = Session()

config_service = ConfigService()
limit_service = LimitService(config_service, session)
config_service.make_config()


while True:
    x = input().split(',')
    print(limit_service.check_limit(x[0], x[1]))