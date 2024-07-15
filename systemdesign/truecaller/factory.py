class ServiceFactory:
    @staticmethod
    def get_service(service_type: str):
        if service_type == 'user':
            return UserServiceImpl()
        elif service_type == 'contact':
            return ContactServiceImpl()
        elif service_type == 'caller_id':
            return CallerIdServiceImpl()
        elif service_type == 'spam':
            return SpamServiceSingleton.get_instance()
        elif service_type == 'search':
            return SearchServiceImpl()
        else:
            raise ValueError("Unknown service type")
