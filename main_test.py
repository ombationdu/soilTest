import mysql.connector
from farmer_manager import FarmerManager
from county_manager import CountyManager
from soil_test_record_manager import SoilTestingRecordManager
from county_farmer_relationship_managersoil_test_record_manager import CountyFarmerRelationshipManager

class DataManager:
    def __init__(self, host, user, password, database):
        self.host = "127.0.0.1"
        self.user = "ombati"
        self.password = "your_password"
        self.database = "soilTest"
        self.farmer_manager = FarmerManager(host, user, password, database)
        self.county_manager = CountyManager(host, user, password, database)
        self.soil_testing_manager = SoilTestingRecordManager(host, user, password, database)
        self.relationship_manager = CountyFarmerRelationshipManager(host, user, password, database)

    def add_farmer(self, name, address, contact_information, county_id):
        self.farmer_manager.add_farmer(name, address, contact_information, county_id)

    def get_farmer(self, farmer_id):
        return self.farmer_manager.get_farmer(farmer_id)

    def update_farmer(self, farmer_id, name=None, address=None, contact_information=None, county_id=None):
        self.farmer_manager.update_farmer(farmer_id, name, address, contact_information, county_id)

    def delete_farmer(self, farmer_id):
        self.farmer_manager.delete_farmer(farmer_id)

    def add_county(self, county_name, relevant_information=None):
        self.county_manager.add_county(county_name, relevant_information)

    def get_county(self, county_id):
        return self.county_manager.get_county(county_id)

    def update_county(self, county_id, county_name=None, relevant_information=None):
        self.county_manager.update_county(county_id, county_name, relevant_information)

    def delete_county(self, county_id):
        self.county_manager.delete_county(county_id)

    def add_soil_testing_record(self, farmer_id, test_date, soil_quality_parameters, testing_results, relevant_information=None):
        self.soil_testing_manager.add_soil_testing_record(farmer_id, test_date, soil_quality_parameters, testing_results, relevant_information)

    def get_soil_testing_record(self, record_id):
        return self.soil_testing_manager.get_soil_testing_record(record_id)

    def update_soil_testing_record(self, record_id, farmer_id=None, test_date=None, soil_quality_parameters=None, testing_results=None, relevant_information=None):
        self.soil_testing_manager.update_soil_testing_record(record_id, farmer_id, test_date, soil_quality_parameters, testing_results, relevant_information)

    def delete_soil_testing_record(self, record_id):
        self.soil_testing_manager.delete_soil_testing_record(record_id)

    def add_relationship(self, farmer_id, county_id, metadata=None):
        self.relationship_manager.add_relationship(farmer_id, county_id, metadata)

    def get_relationship(self, farmer_id, county_id):
        return self.relationship_manager.get_relationship(farmer_id, county_id)

    def update_relationship(self, farmer_id, county_id, metadata=None):
        self.relationship_manager.update_relationship(farmer_id, county_id, metadata)

    def delete_relationship(self, farmer_id, county_id):
        self.relationship_manager.delete_relationship(farmer_id, county_id)

    def __del__(self):
        del self.farmer_manager
        del self.county_manager
        del self.soil_testing_manager
        del self.relationship_manager

