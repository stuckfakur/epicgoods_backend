from repositories.FollowerRepository import FollowerRepository

class FollowerService:
    @staticmethod
    def get_all_follower():
        follower = FollowerRepository.get_all_follower()
        return [follower.to_dict() for follower in follower]
    
    @staticmethod
    def get_follower_by_id(id):
        return FollowerRepository.get_follower_by_id(id)

    @staticmethod
    def create_follower(
        user_id,
        followers_id
    ):
        return FollowerRepository.create_follower(
            user_id,
            followers_id
        )