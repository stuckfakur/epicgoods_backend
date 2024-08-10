from repositories.SellerReposirory import SellerRepository

class Validator:
    @staticmethod
    def validate_seller(store_name, store_info, description):
        if not store_name or not isinstance(store_name, str):
            raise ValueError("seller data is required")
        if not store_info or not isinstance(store_info, str):
            raise ValueError("seller data is required")
        if not description or not isinstance(description, str):
            raise ValueError("seller data is required")

class SellerService:
    @staticmethod
    def get_all_seller(sort=None, order='asc'):
        seller = SellerRepository.get_all_seller(sort, order)
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