
class Preprocessor:
    
    def __init__(self):
        self.data=None
        self._preprocessor=Pre_processing()

    def _process(self, data, ntrain):

        self.data=data

        self.ntrain=ntrain
        
        cols_drop=['Unnamed: 0']
        
        # Numeric columns
        num_cols = ['Cylinders','Valves_Per_Cylinder','Doors','Gears','Seating_Capacity','Number_of_Airbags',
                    'USB_Ports']

        # Categorical columns
        cat_cols = ['Make','Model','Variant','Displacement','Drivetrain','Cylinder_Configuration','Emission_Norm',
                    'Engine_Location', 'Fuel_System','Fuel_Tank_Capacity','Fuel_Type','Height','Length','Width',
                    'Body_Type', 'City_Mileage','Highway_Mileage','ARAI_Certified_Mileage','ARAI_Certified_Mileage_for_CNG',
                    'Kerb_Weight','Ground_Clearance','Front_Brakes', 'Rear_Brakes','Front_Suspension','Rear_Suspension',
                    'Front_Track','Rear_Track','Front_Tyre_&_Rim','Rear_Tyre_&_Rim', 'Power_Steering','Power_Windows',
                    'Power_Seats','Keyless_Entry','Power','Torque', 'Odometer','Speedometer','Tachometer','Tripmeter',
                    'Seats_Material','Type','Wheelbase','Wheels_Size', 'Start_/_Stop_Button','12v_Power_Outlet', 'Audiosystem'
                    'Aux-in_Compatibility','Average_Fuel_Consumption','Basic_Warranty','Bluetooth','Boot-lid_Opener',
                    'Boot_Space','CD_/_MP3_/_DVD_Player','Central_Locking','Child_Safety_Locks','Clock','Cup_Holders',
                    'Distance_to_Empty','Door_Pockets','Engine_Malfunction_Light','Extended_Warranty','FM_Radio',
                    'Fuel-lid_Opener','Fuel_Gauge','Handbrake','Instrument_Console','Low_Fuel_Warning',
                    'Minimum_Turning_Radius','Multifunction_Display','Sun_Visor','Third_Row_AC_Vents','Ventilation_System',
                    'Auto-Dimming_Rear-View_Mirror','Hill_Assist','Gear_Indicator','3_Point_Seat-Belt_in_Middle_Rear_Seat',
                    'Ambient_Lightning','Cargo/Boot_Lights','Drive_Modes','Engine_Immobilizer','High_Speed_Alert_System',
                    'Lane_Watch_Camera/_Side_Mirror_Camera','Passenger_Side_Seat-Belt_Reminder','Seat_Back_Pockets',
                    'Voice_Recognition','Walk_Away_Auto_Car_Lock','ABS_(Anti-lock_Braking_System)','Headlight_Reminder',
                    'Adjustable_Headrests','Gross_Vehicle_Weight','Airbags','Door_Ajar_Warning',
                    'EBD_(Electronic_Brake-force_Distribution)','Fasten_Seat_Belt_Warning','Gear_Shift_Reminder',
                    'Compression_Ratio','Adjustable_Steering_Column','Other_Specs','Other_specs','Parking_Assistance',
                    'Key_Off_Reminder','USB_Compatibility','Android_Auto','Apple_CarPlay','Cigarette_Lighter',
                    'Infotainment_Screen','Multifunction_Steering_Wheel','Average_Speed','EBA_(Electronic_Brake_Assist)',
                    'Seat_Height_Adjustment','Navigation_System','Second_Row_AC_Vents','Tyre_Pressure_Monitoring_System',
                    'Rear_Center_Armrest','iPod_Compatibility','ESP_(Electronic_Stability_Program)','Cooled_Glove_Box',
                    'Recommended_Tyre_Pressure','Heated_Seats','Turbocharger','ISOFIX_(Child-Seat_Mount)','Rain_Sensing_Wipers',
                    'Paddle_Shifters','Leather_Wrapped_Steering','Automatic_Headlamps','Engine_Type','ASR_/_Traction_Control',
                    'Cruise_Control','Heads-Up_Display','Welcome_Lights','Battery','Electric_Range']
        
        drop_strategies=[(cols_drop,1)]

        fill_strategies=[(['BsmtFinType2','BsmtQual','BsmtCond','ExterQual','ExterCond','MasVnrArea',
                          'TotalBsmtSF','HeatingQC','BsmtHalfBath','BsmtFinSF1','BsmtFinSF2','GarageYrBlt',
                          'BsmtFullBath','BsmtUnfSF','GarageCars','GarageArea','MasVnrArea'],0),
                         (['FireplaceQu','GarageQual','GarageCond','BsmtFinType1','MasVnrType',
                          'BsmtExposure','GarageFinish','PoolQC','Fence','LandSlope','GarageType',
                          'LotShape','PavedDrive','Street','Alley','CentralAir','MiscFeature',
                          'MSSubClass','OverallCond','YrSold','MoSold'],'NA'),
                         (['Functional'],'Typ'), # Typical Functionality
                         (['KitchenQual'],'TA'),
                         (['LotFrontage'],'median'),
                         (['MSZoning'],'mode'),
                         (['SaleType','Exterior1st','Exterior2nd','SaleType'],'Oth'), #other
                         (['Electrical'],'SBrkr')]  # Standard Circuit Breakers & Romex

        #drop
        self.data = self._preprocessor.drop(self.data, drop_strategies)
        
        #fill nulls
        self.data = self._preprocessor.fillna(self.ntrain, fill_strategies)
        
        #feature engineering
        self.data = self._preprocessor.feature_engineering()
        
        #label encoder
        self.data = self._preprocessor.label_encoder(cat_cols)
        
        #normalizing
#         self.data = self._preprocessor.norm_data(self.data, num_cols)
        
        #get dummies
        self.data = self._preprocessor.get_dummies(cat_cols)
        return self.data
        