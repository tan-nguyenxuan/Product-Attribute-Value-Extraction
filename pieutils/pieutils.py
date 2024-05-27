from itertools import product
import json

category_attribute_2_human = {
    'Flash Memory Cards_SD Format':['8GB microSD memory for LG VX9700 Dare Phone', 'Transcend TS16GSDHC6V 16 GB SDHC HD Video Card', 'Lexar LCF2GBDRBNA233 2GB Professional 233x CompactFlash Card'],
    'Flash Memory Cards_Capacity':['Professional Ultra SanDisk 200GB MicroSDXC Yarvik TAB13-201 card is custom formatted for high speed up to 90MB/s with lossless recording! Includes Standard SD Adapter. [Newest Version]', 'Viking 128 MB CompactFlash Card for Compaq Products (C470128CF)', 'Silicon Power High Endurance MLC MicroSDHC Memory Card for Dash Cam and Security Camera, with Adapter'],
    'Digital Cameras_Optical Zoom':['Nikon Coolpix 885 3MP Digital Camera w/ 3x Optical Zoom', 'Nikon Coolpix S1 5.1 MP Slim-Design Digital Camera with 3x Optical Zoom (Includes Dock) (OLD MODEL)', 'Vivitar ViviCam 5118 - 5.1 Megapixels 4x Digital Zoom - Color : Pink'],
    'Digital Cameras_Camera Weight':['Nikon Coolpix 885 3MP Digital Camera w/ 3x Optical Zoom', 'Nikon Coolpix S1 5.1 MP Slim-Design Digital Camera with 3x Optical Zoom (Includes Dock) (OLD MODEL)', 'Vivitar ViviCam 5118 - 5.1 Megapixels 4x Digital Zoom - Color : Pink'],
    'Digital Cameras_Resolution':['Pentax Optio 230 2MP Digital Camera w/ 3x Optical Zoom', 'Nikon Coolpix 885 3MP Digital Camera w/ 3x Optical Zoom', 'Cobra 3-in-1 VGA Digital Camera DC345 (Discontinued by Manufacturer)'],
    'Digital Cameras_Sensor Size':['Sony a7 Full-Frame Mirrorless Digital Camera with 28-70mm Lens', 'Nikon D90 DX-Format 12.3MP Digital SLR Camera with 18-105mm f/3.5-5.6G ED AF-S VR DX Nikkor Zoom Lens, and 70-300mm f/4.5-5.6G ED-IF AF-S \"VR\" Zoom Nikkor Lens + 8GB Deluxe Accessory Kit', 'Cobra 3-in-1 VGA Digital Camera DC345 (Discontinued by Manufacturer)'],
    'Digital Cameras_Sensor Type':['Nikon D3300 24.2 MP CMOS Digital SLR Body Only (Black) Bundle 1', 'Nikon Coolpix 885 3MP Digital Camera w/ 3x Optical Zoom', 'Nikon Coolpix S1 5.1 MP Slim-Design Digital Camera with 3x Optical Zoom (Includes Dock) (OLD MODEL)'],
    'Laptops_Processor Brand':['Dell Inspiron 14z i14z-2100sLV 14.0-Inch Ultrabook (1.9 GHz Intel Core i3-3227U Processor, 6GB DDR3, 500GB HDD, Windows 8) Moon Silver [Discontinued By Manufacturer]', 'HP NW9440 17.0 Inch Laptop, Intel Core 2 Duo T7400 2.16 GHz, 2 GB DDR2 SDRAM, 100 GB Hard Drive, Genuine Windows XP Professional (SP2)', 'OQO 1070103-US Model 02 5\" Ultra Mobile PC UMPC'],
    'Laptops_Resolution':['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'Dell XPS 17 Laptop, i7-2630QM, 8GB DDR3 Memory, 17.3in FHD WLED AG (1920x1080) Screen, NVIDIA GeForce GT 555M 3GB graphics with Optimus, 1TB 7200 RPM Hard Drive, Tray Load Blu-ray Disc BD-Combo, Windows 7 Home Premium, 1 Year Limited Warranty', 'NE52215u-45004G50Mnsk 15.6\" LED AMD A-Series A4-5000 1.50 GHz 4GB RAM 500 GB HDD Windows 8 64bit Silver Notebook(Certified Refurbished)'],
    'Laptops_Battery Life':['Gateway EC1430U 11.6-Inch Black Laptop - Up to 7 Hours of Battery Life (Windows 7 Home Premium)', 'Acer Aspire One AOD250-1289 10.1-Inch Seashell White Netbook - 6.5 Hour Battery Life', 'Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White'],
    'Laptops_Number of Cores':['HP Pavilion dv6113us 15.4\" Notebook Laptop PC (AMD Turion 64 X2 Dual-Core TL-50 1.6GHz, 1GB RAM, 80GB HDD / DVD\u00b1RW DL / Wireless / WXP Media Center) by CE', 'ASUS N61JQ-X1 16-Inch Laptop (1.6 GHz Intel Core i7-720QM Quad-Core Processor, 4GB DDR3, 320GB HDD, Windows 7 Home Premium) Dark Brown', 'Apple MacBook MA472LL/A 13.3\" Laptop (2.0 GHz Intel Core Duo, 512 MB RAM, 80 GB Hard Drive, SuperDrive)-Black'],
    'Laptops_Processor Speed':['HP Pavilion dv6113us 15.4\" Notebook Laptop PC (AMD Turion 64 X2 Dual-Core TL-50 1.6GHz, 1GB RAM, 80GB HDD / DVD\u00b1RW DL / Wireless / WXP Media Center) by CE', 'Dell Inspiron 14z i14z-2100sLV 14.0-Inch Ultrabook (1.9 GHz Intel Core i3-3227U Processor, 6GB DDR3, 500GB HDD, Windows 8) Moon Silver [Discontinued By Manufacturer]', 'Averatec AV3255P1-01 Laptop (AMD Athlon XP-M 2000+, 512 MB RAM, 40 GB Hard drive, 802.11g, DVD+CD-RW combo)'],
    'Laptops_Screen Size':['HP Pavilion dv6113us 15.4\" Notebook Laptop PC (AMD Turion 64 X2 Dual-Core TL-50 1.6GHz, 1GB RAM, 80GB HDD / DVD\u00b1RW DL / Wireless / WXP Media Center) by CE', 'Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'Toshiba A45-S121 Laptop (2.8 GHz Celeron, 256 MB RAM, 40 GB Hard Drive, DVD/CD-RW Combo)'],
    'Laptops_Weight':['HP Pavilion dv6113us 15.4\" Notebook Laptop PC (AMD Turion 64 X2 Dual-Core TL-50 1.6GHz, 1GB RAM, 80GB HDD / DVD\u00b1RW DL / Wireless / WXP Media Center) by CE', 'Dell Inspiron 14z i14z-2100sLV 14.0-Inch Ultrabook (1.9 GHz Intel Core i3-3227U Processor, 6GB DDR3, 500GB HDD, Windows 8) Moon Silver [Discontinued By Manufacturer]', 'Averatec AV3255P1-01 Laptop (AMD Athlon XP-M 2000+, 512 MB RAM, 40 GB Hard drive, 802.11g, DVD+CD-RW combo)'],
    'Laptops_Refresh Rate':['HP Pavilion dv6113us 15.4\" Notebook Laptop PC (AMD Turion 64 X2 Dual-Core TL-50 1.6GHz, 1GB RAM, 80GB HDD / DVD\u00b1RW DL / Wireless / WXP Media Center) by CE', 'Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'Toshiba A45-S121 Laptop (2.8 GHz Celeron, 256 MB RAM, 40 GB Hard Drive, DVD/CD-RW Combo)'],
}

category_attribute_2_system = {
    'Flash Memory Cards_SD Format': ['MicroSD', 'SDHC', 'I do not know.'],
    'Flash Memory Cards_Capacity': ['200GB', '128MB', 'I do not know.'],
    'Digital Cameras_Optical Zoom':['3x', '3x', 'I do not know.'],
    'Digital Cameras_Camera Weight':['I do not know.', 'I do not know.', 'I do not know.'],
    'Digital Cameras_Resolution': ['2MP', '3MP', 'I do not know.'],
    'Digital Cameras_Sensor Size': ['Full-Frame', 'DX-Format', 'I do not know.'],
    'Digital Cameras_Sensor Type': ['CMOS', 'I do not know.', 'I do not know.'],
    'Laptops_Processor Brand': ['Intel', 'Intel', 'I do not know.'],
    'Laptops_Resolution':['FHD 1080P', '1920x1080', 'I do not know.'],
    'Laptops_Battery Life':['7 Hours', '6.5 Hours', 'I do not know.'],
    'Laptops_Number of Cores':['2', '4', 'I do not know.'],
    'Laptops_Processor Speed':['1.6GHz', '1.9 GHz', 'I do not know.'],
    'Laptops_Screen Size':['15.4 inches', '13.3 inches', 'I do not know.'],
    'Laptops_Weight':['I do not know.', 'I do not know.', 'I do not know.'],
    'Laptops_Refresh Rate':['I do not know.', 'I do not know.', 'I do not know.']
}

category_attribute_2_human_msg = {
    'Flash Memory Cards_SD Format': ['16GB MicroSDHC Memory Card for AT&T LG Xpression C395 Smartphone with Free USB MicroSD/SDHC Card Reader -- 16 G/GB/GIG 16G 16GIG','Professional Ultra SanDisk 64GB MicroSDXC Sony PlayStation Portable 3000 Series card is custom formatted for high speed, lossless recording! Includes Standard SD Adapter. (UHS-1 Class 10 Certified 30MB/sec)', 'Transcend TS16GSDHC6V 16 GB SDHC HD Video Card'],
    'Flash Memory Cards_Capacity': ['16GB MicroSDHC Memory Card for AT&T LG Xpression C395 Smartphone with Free USB MicroSD/SDHC Card Reader -- 16 G/GB/GIG 16G 16GIG','Professional Ultra SanDisk 64GB MicroSDXC Sony PlayStation Portable 3000 Series card is custom formatted for high speed, lossless recording! Includes Standard SD Adapter. (UHS-1 Class 10 Certified 30MB/sec)', 'Transcend TS16GSDHC6V 16 GB SDHC HD Video Card'],
    'Digital Cameras_Optical Zoom': ['Pentax Optio 230 2MP Digital Camera w/ 3x Optical Zoom','Nikon Coolpix 885 3MP Digital Camera w/ 3x Optical Zoom','Vivitar ViviCam 5118 - 5.1 Megapixels 4x Digital Zoom - Color : Pink'],
    'Digital Cameras_Camera Weight': ['Pentax Optio 230 2MP Digital Camera w/ 3x Optical Zoom','Nikon Coolpix 885 3MP Digital Camera w/ 3x Optical Zoom','Vivitar ViviCam 5118 - 5.1 Megapixels 4x Digital Zoom - Color : Pink'],
    'Digital Cameras_Resolution': ['Pentax Optio 230 2MP Digital Camera w/ 3x Optical Zoom','Vivitar ViviCam 5118 - 5.1 Megapixels 4x Digital Zoom - Color : Pink','Cobra 3-in-1 VGA Digital Camera DC345 (Discontinued by Manufacturer)'],
    'Digital Cameras_Sensor Size': ['Sony a7 Full-Frame Mirrorless Digital Camera with 28-70mm Lens', 'Minolta Dimage 1500 1.5MP Digital Camera w/ 3x Optical Zoom', 'Agfa 1680 1.2MP Digital Camera w/ 3x Optical Zoom'],
    'Digital Cameras_Sensor Type': ['Nikon D3300 24.2 MP CMOS Digital SLR Body Only (Black) Bundle 1', 'Agfa 1680 1.2MP Digital Camera w/ 3x Optical Zoom', 'Kodak DC260 1.6 MP Digital Camera with 3xOptical Zoom'],
    'Laptops_Processor Brand': ['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black', 'Apple Powerbook Laptop (400-MHz PowerPC G4, 128 MB RAM, 10 GB hard drive)'],
    'Laptops_Resolution': ['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White','ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black','Compaq Presario 2700US Laptop (1-GHz Pentium III, 256 MB RAM, 20 GB hard drive)'],
    'Laptops_Battery Life': ['Gateway EC1430U 11.6-Inch Black Laptop - Up to 7 Hours of Battery Life (Windows 7 Home Premium)', 'Acer Aspire One AOD250-1289 10.1-Inch Seashell White Netbook - 6.5 Hour Battery Life', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black'],
    'Laptops_Number of Cores': ['HP Pavilion dv6113us 15.4\" Notebook Laptop PC (AMD Turion 64 X2 Dual-Core TL-50 1.6GHz, 1GB RAM, 80GB HDD / DVD\u00b1RW DL / Wireless / WXP Media Center) by CE', 'Apple MacBook Pro 15.4\" Laptop - 500 GB HARDRIVE - i7 QUAD-CORE - MC721LL/A', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black'],
    'Laptops_Processor Speed': ['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black', 'Dell Latitude CPX Notebook (Pentium III, 128 MB RAM, 12 GB hard drive)'],
    'Laptops_Screen Size': ['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black', 'Compaq Presario 2700US Laptop (1-GHz Pentium III, 256 MB RAM, 20 GB hard drive)'],
    'Laptops_Weight': ['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black', 'Apple iBook Laptop (500-MHz PowerPC G3, 64 MB RAM, 10 GB hard drive)'],
    'Laptops_Refresh Rate': ['Acer Aspire S7 13.3-Inch Touchscreen Ultrabook (Intel Core i5-4200U Processor up to 2.6GHz, 8GB DDR3 Memory, 256GB SSD, FHD 1080P Touchscreen Display, Backlit Keyboard, 802.11AC WiFi, Windows 8.1, 0.5 inch thin and 2.9 Lbs) Crystal White', '2018 Newest Flagship Asus ROG Strix 17.3 Full HD 120Hz VR Ready Gaming Laptop (i5-2430M | 8GB RAM | 640GB HDD | Windows 7 Home)', 'ThinkPad T22 2647 - PIII 900 MHz - RAM 128 MB - HDD 20 GB - DVD - Savage/IX - Win2000 Pro - 14.1\" TFT 1024 x 768 ( XGA ) - black']
}

category_attribute_2_system_msg = {
    'Flash Memory Cards_SD Format': ['Capacity: 16GB \n SD Format: MicroSDHC \n Compatibility: AT&T LG Xpression C395 Smartphone \n Included Items: Free USB MicroSD/SDHC Card Reader', 'Brand: SanDisk \n Capacity: 64GB \n Compatibility: Sony PlayStation Portable 3000 Series \n SD Format: MicroSDXC \n Speed: High speed, lossless recording \n Class: UHS-1 Class 10', 'Capacity: 16 GB \n SD Format: SDHC \n Application: HD Video'],
    'Flash Memory Cards_Capacity': ['Capacity: 16GB \n SD Format: MicroSDHC \n Compatibility: AT&T LG Xpression C395 Smartphone \n Included Items: Free USB MicroSD/SDHC Card Reader','Brand: SanDisk \n Capacity: 64GB \n Compatibility: Sony PlayStation Portable 3000 Series \n SD Format: MicroSDXC \n Speed: High speed, lossless recording \n Class: UHS-1 Class 10', 'Capacity: 16 GB \n SD Format: SDHC \n Application: HD Video'],
    'Digital Cameras_Optical Zoom': ['Brand: Pentax \n Model: Optio 230 \n Resolution: 2MP \n Optical Zoom: 3x','Brand: Nikon \n Model: Coolpix 885 \n Resolution: 3MP \n Optical Zoom: 3x','Brand: Vivitar \n Model: ViviCam 5118 \n Megapixels: 5.1 \n Digital Zoom: 4x \n Color: Pink'],
    'Digital Cameras_Camera Weight': ['Brand: Pentax \n Model: Optio 230 \n Resolution: 2MP \n Optical Zoom: 3x','Brand: Nikon \n Model: Coolpix 885 \n Resolution: 3MP \n Optical Zoom: 3x','Brand: Vivitar \n Model: ViviCam 5118 \n Megapixels: 5.1 \n Digital Zoom: 4x \n Color: Pink'],
    'Digital Cameras_Resolution': ['Brand: Pentax \n Model: Optio 230 \n Resolution: 2MP \n Optical Zoom: 3x', 'Brand: Vivitar \n Model: ViviCam 5118 \n Resolution: 5.1MP \n Digital Zoom: 4x \n Color: Pink', 'Brand: Cobra \n Model: DC345 \n Type: Digital Camera \n Interface: VGA \n Functionality: 3-in-1 \n Discontinued by Manufacturer: Yes'],
    'Digital Cameras_Sensor Size': ['Model: Sony a7 \n Type: Full-Frame Mirrorless Digital Camera \n Lens: 28-70mm \n Sensor Size: Full-Frame', 'Optical Zoom : 3x Optical Zoom \n Resolution : 1.5MP', 'Optical Zoom : 3x Optical Zoom'],
    'Digital Cameras_Sensor Type': ['Brand: Nikon \n Model: D3300 \n Sensor Type: CMOS \n Megapixels: 24.2 \n Camera Type: Digital SLR \n Color: Black \n Bundle Included: 1', 'Optical Zoom : 3x Optical Zoom', 'Resolution : 1.6 MP'],
    'Laptops_Processor Brand': ['Brand: Acer \n Model: Aspire S7 \n Screen Size: 13.3 inches \n Screen Type: Touchscreen \n Processor: Intel Core i5-4200U \n Processor Brand: Intel \n Processor Speed: 2.6GHz \n Memory: 8GB DDR3 \n Storage: 256GB SSD \n Resolution: FHD 1080P \n Keyboard: Backlit\n Wireless Connectivity: 802.11AC WiFi \n Operating System: Windows 8.1 \n Color: Crystal White \n Thickness: 0.5 inch \n Weight: 2.9 lbs', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768', 'Brand: Apple \n Model: Powerbook Laptop \n Processor: 400-MHz PowerPC G4 \n RAM: 128 MB \n Hard Drive Capacity: 10 GB'],
    'Laptops_Resolution': ['Brand: Acer \n Model: Aspire S7 \n Screen Size: 13.3 inches \n Screen Type: Touchscreen \n Processor: Intel Core i5-4200U \n Processor Brand: Intel \n Processor Speed: 2.6GHz \n Memory: 8GB DDR3 \n Storage: 256GB SSD \n Resolution: FHD 1080P \n Keyboard: Backlit\n Wireless Connectivity: 802.11AC WiFi \n Operating System: Windows 8.1 \n Color: Crystal White \n Thickness: 0.5 inch \n Weight: 2.9 lbs', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768', 'Processor Speed : 1-GHz \n Processor Brand : Pentium'],
    'Laptops_Battery Life': ['Model: Gateway EC1430U \n Color: Black \n Screen size: 11.6 inches \n Operating System: Windows 7 Home Premium \n Battery Life: 7 Hours','Screen Size : 10.1-Inch \n Battery Life : 6.5 Hours', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768'],
    'Laptops_Number of Cores': ['Brand: HP \n Model: Pavilion dv6113us \n Screen Size: 15.4 inches \n Processor: AMD Turion 64 X2 Dual-Core TL-50 1.6GHz \n Number of Cores: 2 \n RAM: 1GB \n Hard Drive: 80GB HDD \n Optical Drive: DVD\u00b1RW DL \n Wireless: Yes \n Operating System: Microsoft Windows XP Media Center', 'Number of Cores : 4 \n Screen Size : 15.4\" \n Processor Brand : CORE', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768'],
    'Laptops_Processor Speed': ['Brand: Acer \n Model: Aspire S7 \n Screen Size: 13.3 inches \n Screen Type: Touchscreen \n Processor: Intel Core i5-4200U \n Processor Brand: Intel \n Processor Speed: 2.6GHz \n Memory: 8GB DDR3 \n Storage: 256GB SSD \n Resolution: FHD 1080P \n Keyboard: Backlit\n Wireless Connectivity: 802.11AC WiFi \n Operating System: Windows 8.1 \n Color: Crystal White \n Thickness: 0.5 inch \n Weight: 2.9 lbs', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768', 'Processor Brand : Pentium'],
    'Laptops_Screen Size': ['Brand: Acer \n Model: Aspire S7 \n Screen Size: 13.3 inches \n Screen Type: Touchscreen \n Processor: Intel Core i5-4200U \n Processor Brand: Intel \n Processor Speed: 2.6GHz \n Memory: 8GB DDR3 \n Storage: 256GB SSD \n Resolution: FHD 1080P \n Keyboard: Backlit\n Wireless Connectivity: 802.11AC WiFi \n Operating System: Windows 8.1 \n Color: Crystal White \n Thickness: 0.5 inch \n Weight: 2.9 lbs', 'Screen Size : 14.1 inches \n Processor Speed : 900 MHz \n Resolution : 1024 x 768', 'Processor Speed : 1-GHz \n Processor Brand : Pentium'],
    'Laptops_Weight': ['Brand: Acer \n Model: Aspire S7 \n Screen Size: 13.3 inches \n Screen Type: Touchscreen \n Processor: Intel Core i5-4200U \n Processor Brand: Intel \n Processor Speed: 2.6GHz \n Memory: 8GB DDR3 \n Storage: 256GB SSD \n Resolution: FHD 1080P \n Keyboard: Backlit\n Wireless Connectivity: 802.11AC WiFi \n Operating System: Windows 8.1 \n Color: Crystal White \n Thickness: 0.5 inch \n Weight: 2.9 lbs', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768', 'Processor Speed : 500-MHz'],
    'Laptops_Refresh Rate': ['Brand: Acer \n Model: Aspire S7 \n Screen Size: 13.3 inches \n Screen Type: Touchscreen \n Processor: Intel Core i5-4200U \n Processor Brand: Intel \n Processor Speed: 2.6GHz \n Memory: 8GB DDR3 \n Storage: 256GB SSD \n Resolution: FHD 1080P \n Keyboard: Backlit\n Wireless Connectivity: 802.11AC WiFi \n Operating System: Windows 8.1 \n Color: Crystal White \n Thickness: 0.5 inch \n Weight: 2.9 lbs', 'Refresh Rate : 120Hz', 'Screen Size : 14.1\" \n Processor Speed : 900 MHz \n Resolution : 1024 x 768']
}

# Update Task Dict
def update_task_dict_from_file(file_name, task_dict, flag):
    with open(file_name, 'r') as f:
        for line in f:
            record = json.loads(line)
            example = {}
            for attribute in record['attributes']:
                if attribute['key'] != record['attribute']:
                    continue
                
                if(flag == False):
                    if(task_dict['shots'] == 1):
                        example['human_0'] = category_attribute_2_human_msg['{}_{}'.format(record['category'], attribute['key'])][0]
                        example['system_0'] = category_attribute_2_system_msg['{}_{}'.format(record['category'], attribute['key'])][0]
                    elif(task_dict['shots'] == 3):
                        for i in range(0, task_dict['shots']):
                            example['human_{}'.format(str(i))] = category_attribute_2_human_msg['{}_{}'.format(record['category'], attribute['key'])][i]
                            example['system_{}'.format(str(i))] = category_attribute_2_system_msg['{}_{}'.format(record['category'], attribute['key'])][i]     
                else:
                    if(task_dict['shots'] == 1):
                        example['human_0'] = '{} \n Requested Attribute: {}'.format(category_attribute_2_human['{}_{}'.format(record['category'], attribute['key'])][0], record['category'])
                        example['system_0'] = category_attribute_2_system['{}_{}'.format(record['category'], attribute['key'])][0]
                    elif(task_dict['shots'] == 3):
                        for i in range(0, task_dict['shots']):
                            example['human_{}'.format(str(i))] = '{} \n Requested Attribute: {}'.format(category_attribute_2_human['{}_{}'.format(record['category'], attribute['key'])][i], record['category'])
                            example['system_{}'.format(str(i))] = category_attribute_2_system['{}_{}'.format(record['category'], attribute['key'])][i]
                    
                if flag == True:
                    example['input'] = '{} \n Requested Attribute: {}'.format(record['title'], attribute['key'])
                else:
                    example['input'] = record['title']
                example['category'] = record['category']
                example['attribute'] = attribute['key']
                example['target_scores'] = {}

                for evidence in attribute['evidences']:
                    if evidence['pid'] == 0:
                        example['target_scores'][evidence['value']] = 1
                if len(example['target_scores']) == 0:
                    example['target_scores']['I do not know.'] = 1
                task_dict['examples'].append(example)
    return task_dict

def combine_example(example, pred, post_pred):
    """Format examples to save the predictions"""
    example['pred'] = pred
    example['post_pred'] = post_pred
    return example


def calculate_recall_precision_f1(targets, preds, categories, attributes):
    """Calculate recall, precision and f1 for the extractions."""
    unique_attributes = list(set(attributes))
    unique_categories = list(set(categories))

    result_dict = {}
    total_eval_nn = 0  # the model can predict No value (I do not know.) when ground truth is No attribute value
    total_eval_nv = 0  # some incorrect Value when ground truth is No attribute value
    total_eval_vn = 0  # the model can predict No value (I do not know.) when the ground truth has attribute Values
    total_eval_vc = 0  # Correct values when the ground truth has attribute Values
    total_eval_vw = 0  # Wrong values when the ground truth has attribute Values

    for unique_category in unique_categories:
        for unique_attribute in unique_attributes:

            eval_nn = 0  # the model can predict No value (I do not know.) when ground truth is No attribute value
            eval_nv = 0  # some incorrect Value when ground truth is No attribute value
            eval_vn = 0  # the model can predict No value (I do not know.) when the ground truth has attribute Values
            eval_vc = 0  # Correct values when the ground truth has attribute Values
            eval_vw = 0  # Wrong values when the ground truth has attribute Values

            for target, pred, category, attribute in zip(targets, preds, categories, attributes):
                if unique_attribute != attribute or unique_category != category:
                    # Evaluate per attribute/category
                    continue

                target_values = [value if value != "I do not know." else None for value in target]
                prediction = pred if pred != "I do not know." else None

                if target_values[0] is None and prediction is None:
                    eval_nn += 1
                elif target_values[0] is None and prediction is not None:
                    eval_nv += 1
                elif target_values[0] is not None and prediction is None:
                    eval_vn += 1
                elif prediction in target_values:
                    eval_vc += 1
                else:
                    eval_vw += 1

            precision = round((eval_vc / (eval_nv + eval_vc + eval_vw)) * 100, 2) if (
                                                                                                 eval_nv + eval_vc + eval_vw) > 0 else 0
            recall = round((eval_vc / (eval_vn + eval_vc + eval_vw)) * 100, 2) if (
                                                                                              eval_vn + eval_vc + eval_vw) > 0 else 0
            f1 = round(2 * precision * recall / (precision + recall), 2) if (precision + recall) > 0 else 0

            total_eval_nn += eval_nn
            total_eval_nv += eval_nv
            total_eval_vn += eval_vn
            total_eval_vc += eval_vc
            total_eval_vw += eval_vw

            if (eval_nv + eval_vc + eval_vw) == 0 and (eval_vn + eval_vc + eval_vw) == 0:
                # Combination does not exist
                continue

            result_dict['{}_{}'.format(unique_attribute, unique_category)] = {'precision': precision, 'recall': recall,
                                                                              'f1': f1}

            print('Attribute: {} - Category: {}'.format(unique_attribute, unique_category))
            print(result_dict['{}_{}'.format(unique_attribute, unique_category)])

    # Calculate macro scores
    precision_scores = [result_dict['{}_{}'.format(attribute, category)]['precision'] for attribute, category in
                        product(unique_attributes, unique_categories)
                        if '{}_{}'.format(attribute, category) in result_dict]
    macro_precision = round(sum(precision_scores) / len(precision_scores), 2)

    recall_scores = [result_dict['{}_{}'.format(attribute, category)]['recall'] for attribute, category in
                     product(unique_attributes, unique_categories)
                     if '{}_{}'.format(attribute, category) in result_dict]
    macro_recall = round(sum(recall_scores) / len(recall_scores), 2)

    f1_scores = [result_dict['{}_{}'.format(attribute, category)]['f1'] for attribute, category in
                 product(unique_attributes, unique_categories)
                 if '{}_{}'.format(attribute, category) in result_dict]
    macro_f1 = round(sum(f1_scores) / len(f1_scores), 2)

    # Calculate micro scores
    micro_precision = round((total_eval_vc / (total_eval_nv + total_eval_vc + total_eval_vw)) * 100, 2) if (
                                                                                                                       total_eval_nv + total_eval_vc + total_eval_vw) > 0 else 0
    micro_recall = round((total_eval_vc / (total_eval_vn + total_eval_vc + total_eval_vw)) * 100, 2) if (
                                                                                                                    total_eval_vn + total_eval_vc + total_eval_vw) > 0 else 0
    micro_f1 = round(2 * micro_precision * micro_recall / (micro_precision + micro_recall), 2) if (
                                                                                                              micro_precision + micro_recall) > 0 else 0

    result_dict['macro'] = {'macro_precision': macro_precision, 'macro_recall': macro_recall, 'macro_f1': macro_f1}
    result_dict['micro'] = {'micro_precision': micro_precision, 'micro_recall': micro_recall, 'micro_f1': micro_f1}

    print('Macro:')
    print(result_dict['macro'])
    print('Micro:')
    print(result_dict['micro'])

    return result_dict

def parse_gpt_response_to_dict(response):
    # Split Response by new line
    response_parts = response.split('\n')
    response_parts = [part.strip() for part in response_parts if part.strip() != '']

    # Try to parse line as a JSON object - 2nd attempt
    response_dict = {}

    i = 0

    while i < len(response_parts):
        parsed_response_part = response_parts[i].replace('Human:', '')\
                            .replace('AI:', '').replace('System:', '').strip()
        if ':' in parsed_response_part:
            parsed_response_part = parsed_response_part.split(':')

        if len(parsed_response_part) == 2 and parsed_response_part[1] == " {":
            temp = ""
            i = i + 1
            while response_parts[i] != "}":
                temp = temp + response_parts[i]+" "
                i = i + 1
            response_dict[parsed_response_part[0].replace('"', '').replace("'", "").strip()] = temp.replace('"', '').replace("'", "").replace("[","").replace("]","").strip().rstrip(',!')
        elif len(parsed_response_part) == 2 and isinstance(parsed_response_part[0], str) and isinstance(parsed_response_part[1], list):
            parse_str = ", ".join(parsed_response_part[1])
            parsed_response_part[1] = parse_str
            response_dict[parsed_response_part[0].replace('"', '').replace("'", "").strip()] = parsed_response_part[1].replace('"', '').replace("'", "").replace("[","").replace("]","").strip().rstrip(',!')
        elif len(parsed_response_part) == 2 and isinstance(parsed_response_part[0], str) and isinstance(parsed_response_part[1], str):
            response_dict[parsed_response_part[0].replace('"', '').replace("'", "").strip()] = parsed_response_part[1].replace('"', '').replace("'", "").replace("[","").replace("]","").strip().rstrip(',!')
        i = i + 1

    return response_dict