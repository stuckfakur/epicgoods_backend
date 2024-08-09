from models.Follower import Follower, db

class FollowerRepository:
    
    @staticmethod
    def get_all_follower():
        return Follower.query.all()
    
    @staticmethod
    def get_follower_by_id(id):
        return Follower.query.get(id)

    @staticmethod
    def create_follower(
        user_id,
        followers_id
    ):
       new_follower = Follower(
           user_id = user_id,
           followers_id = followers_id
       )
       db.session.add(new_follower)
       db.session.commit()
       return new_follower