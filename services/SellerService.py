from repositories.SellerReposirory import SellerRepository

class SellerService:
    @staticmethod
    def get_all_seller():
        seller = SellerRepository.get_all_seller()
        return [seller.to_dict() for seller in seller]
    
    @staticmethod
    def get_seller_by_id(id):
        return SellerRepository.get_seller_by_id(id)

    @staticmethod
    def create_seller(
        store_name,
        store_info,
        description
    ):
        return SellerRepository.create_seller(
            store_name,
            store_info,
            description
        )