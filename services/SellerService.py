from repositories.SellerReposirory import SellerRepository
from utils.exception import NotFoundError
from sqlalchemy.exc import DataError
import re

class Validator:
    @staticmethod
    def seller_validator(store_name, store_info, description):
        if not store_name or not isinstance(store_name, str):
            raise ValueError("seller data is required")
        if not store_info or not isinstance(store_info, str):
            raise ValueError("seller data is required")
        if not description or not isinstance(description, str):
            raise ValueError("seller data is required")
        
        regex_store_name = '^[a-zA-Z0-9]*$'
        if not re.match(regex_store_name, store_name):
            raise ValueError('only alpabeth and number is allowed in store name')
        
    @staticmethod
    def extra_validator(location_id, address):
        if not location_id or not isinstance(location_id, int):
            raise ValueError("Location ID is required")
        if not address or not isinstance(address, str):
            raise ValueError("address is required")
    @staticmethod
    def user_id_validator(user_id):
        if not user_id or not isinstance(user_id, int):
            raise ValueError("User ID is required")

    @staticmethod
    def type_validator(store_type):
        if not store_type or not isinstance(store_type, str):
            raise ValueError("Store Type is required")
        
    @staticmethod
    def existing_store_name(store_name):
        if SellerRepository.existing_store_name(store_name):
            raise ValueError('store name already exist')

class SellerService:
    @staticmethod
    def create_seller(
        user_id,
        location_id,
        address,
        store_name,
        store_info,
        description,
    ):
        Validator.seller_validator(store_name, store_info, description)
        Validator.user_id_validator(user_id)
        Validator.extra_validator(location_id, address)
        Validator.existing_store_name(store_name)
        seller = SellerRepository.create_seller(
            user_id,
            location_id,
            address,
            store_name,
            store_info,
            description,
        )
        return seller
    
    @staticmethod
    def get_all_seller(sort=None, order='asc'):
        seller = SellerRepository.get_all_seller(sort, order)
        return [seller.to_dict() for seller in seller]
    
    @staticmethod
    def get_seller_by_id(id):
        seller = SellerRepository.get_seller_by_id(id)
        if seller:
            return seller.to_dict()
        else:
            return "Seller not Found"
    
    @staticmethod
    def update_seller(sellerId, location_id, address, store_name, store_type, store_info, description):
        Validator.seller_validator(store_name, store_info, description)
        Validator.extra_validator(location_id, address)
        Validator.existing_store_name(store_name)
        seller = SellerService.get_seller_by_id(sellerId)
        if not seller:
            raise NotFoundError("Seller not found")
        try:
            seller = SellerRepository.update_seller(
                sellerId,
                location_id,
                address,
                store_name,
                store_type,
                store_info,
                description
            )
            return seller.to_dict()
        except DataError as e:
            raise ValueError(f"Database error occurred: {str(e)}")
        except Exception as e:
            raise e
    
    @staticmethod
    def update_seller_location_id(sellerId, location_id):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_location_id(sellerId, location_id)
        return seller
    
    @staticmethod
    def update_seller_address(sellerId, address):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_address(sellerId, address)
        return seller
    
    @staticmethod
    def update_seller_store_name(sellerId, store_name):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_store_name(sellerId, store_name)
        return seller
    
    @staticmethod
    def update_seller_store_type(sellerId, store_type):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_store_type(sellerId, store_type)
        return seller

    @staticmethod
    def update_seller_store_info(sellerId, store_info):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_store_info(sellerId, store_info)
        return seller

    @staticmethod
    def update_seller_store_type(sellerId, store_type):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_store_type(sellerId, store_type)
        return seller
    
    @staticmethod
    def update_seller_description(sellerId, description):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_description(sellerId, description)
        return seller
    
    @staticmethod
    def update_seller_store_status(sellerId, store_status):
        data = SellerService.get_seller_by_id(sellerId)
        if not data:
            raise NotFoundError("Seller not found")
        
        seller = SellerRepository.update_seller_store_status(sellerId, store_status)
        return seller
    
    @staticmethod
    def delete_seller(id):
        user = SellerRepository.get_seller_by_id(id)
        if not user:
            raise NotFoundError("Seller not found")
        user = SellerRepository.delete_seller(id)
        return user