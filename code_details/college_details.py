def get_details(pure_maths,applied_maths,physics,chemistry,biology,english,socialstudies,arabic,islamic,hs,physical_education,fine_arts,music,gender,major_program,avm,ed=0,me=0):



    pm=pure_maths 
    am=applied_maths 
    p=physics 
    c=chemistry 
    b=biology 
    e=english
    ar=arabic
    ss=socialstudies
    islamic=islamic   
    avm=avm
    avm_pass=50
    hs=hs
    pe=physical_education 
    fa=fine_arts
    music=music
    

    if major_program=="engineering":
        p_c_both=['SE920', 'BS061', 'BS209', 'BS051', 'BS295', 'BS026', 'BS246', 'BS056', 'BS226', 'BS217', 'BS087', 'BS119', 'BS034', 'BS266', 'BS291', 'BS293', 'BS010', 'BS013', 'BS014', 'BS042', 'BS043', 'BS046', 'SQ200', 'U0101', 'U0801', 'U0201', 'U0301', 'U0401', 'U0501', 'U0601', 'U0701','U1220', 'PDO001', 'VC001', 'VC003', 'VC006', 'VC008', 'VC010', 'VC012', 'VC015']
        
        p_n_both=['Engineering', 'Marine Engineering,Transformational Engineering', 'Process Engineering,Mechanical Engineering,Environmental Engineering', 'Civil Engineering (Structural Engineering, Transportation Engineering, Environmental Engineering, Water Resources Engineering, and Construction Engineering),,Quantity Surveying & Cost Management,,Electronics & Communications Engineering (Telecommunications Engineering and Biomedical Engineering), ,Computer Engineering (Network Engineering and Software Development), ,Electrical Power Engineering (Energy Systems Engineering, Power System Engineering, Instrumentation & Control Engineering),Mechanical Engineering (Industrial Automation & Control and Energy Systems Engineering)', 'Mechanical Engineering', 'Electrical & Computer Engineering,Chemical Engineering,Civil Engineering,Process Metallurgy and Materials Engineering,Mechanical & Electromechanical Engineering', 'Fire Safety Engineering,Mechanical Engineering (Well Engineering)', 'Mechanical Engineering (Automotive)', 'Civil Engineering,Mechanical Engineering,Information and Communication Engineering,Computer Engineering', 'Civil Engineering,Environmental Engineering,Electronics and Communications Engineering', 'Electrical Engineering and Technology', 'Water Science Engineering', 'Mechanical Engineering,Chemical Engineering,Civil Engineering,Electrical and Electronics Engineering,Computer and Communications Engineering', 'Mechanical Engineering and Vehicle Technology,Electronics and Telecommunication Engineering,Automation and Robotics Engineering,Instrumentation and Control Engineering,Building Services Engineering', 'Chemical Engineering', 'Energy Engineering', 'Civil Engineering', 'Electrical Engineering,Computer Engineering,Environmental Engineering', 'Chemical & Petrochemical Engineering', 'Electronics and Telecommunication', 'Civil Engineering,Mechanical Engineering,Electronic and Instrumentation', 'Computer Hardware and Networking or Computer Engineering with Pathway in Information Security, - الشبكات', 'College of Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Engineering', 'Mechanical Engineering', 'Engineering Disciplines', 'Electronics - Draftsmanship', 'Electronics - Draftsmanship', 'Electronics - Draftsmanship', 'Electronics - Draftsmanship', 'Energy - Electronics - Mechatronics', 'Electronics - Draftsmanship', 'Electronics']
   
        
        h_n_both=['Kuwait University', 'International Maritime College Oman', 'German University of Technology', 'National University of Science and Technology', 'Sur University College', 'Sohar University', 'International College of Engineering and Management', 'National College of Automotive Technology', 'Al Buraimi University', "A'Sharqiyah University", "A'Sharqiyah University", "A'Sharqiyah University", 'Dhofar University', 'Global College of Engineering and Technology', 'Muscat University', 'Muscat University', 'Nizwa University', 'Nizwa University', 'Nizwa University', 'Middle East College', 'Middle East College', 'Middle East College', 'Sultan Qaboos University', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'Private Higher Education Institutes', 'Seeb Vocational College', 'Saham Vocational College', 'Sur Vocational College', 'Ibri Vocational College', 'Shinas Vocational College', 'Buraimi Vocational College', 'Salalah Vocational College']       
       
       
        p_n_a_both=['الهندسة', ' الهندسة البحرية,الهندسة التحويلية', 'هندسة العمليات,الهندسة الميكانيكية,هندسة البيئة', 'الهندسة المدنية (الهندسة الإنشائية ، هندسة النقل ، الهندسة البيئية ، هندسة الموارد المائية ، هندسة البناء),مسح الكميات وإدارة التكاليف,هندسة الإلكترونيات والاتصالات (هندسة الاتصالات والهندسة الطبية الحيوية),هندسة الحاسوب (هندسة الشبكات وتطوير البرمجيات),هندسة القوى الكهربائية (هندسة أنظمة الطاقة ، هندسة أنظمة الطاقة ، هندسة الأجهزة والتحكم),الهندسة الميكانيكية (الأتمتة الصناعية والتحكم وهندسة أنظمة الطاقة)', 'الهندسة الميكانيكية', ' الهندسة الكهربائية والــــــحاســـــب اآللــــــــــــــــي, الهندسة الكيميائية, الهندسة المدنية,هندسة العمليات المعدنية والمــــــواد,الهندسة الميكانيكية والكهروميكانيكية', 'هندسة السلامة من الحرائق,الهندسة الميكانيكية (حفر الآبار)', 'الهندسة الميكانيكية (السيارات)', 'الهندسة المدنية,الهندسة الميكانيكية,هندسة المعلومات واالتصاالت, هندسة الحاسب اآللي', 'الهندسة المدنية,الهندسة البيئية,الهندسة اإللكترونية واإلتصاالت', 'التكنولوجيا في الهندسة الكهربائية', ' العلوم في هندسة المياه', 'الهندسة الميكانيكية,الهندسة الكيميائية,الهندسة المدنية, الهندسة الكهربائية وااللكترونية,هندسة الكمبيوتر واالتصاالت', 'الهندسة الميكانيكية وتكنولوجيا السيارات,الهندسة االلكترونيات واالتصاالت,األتمتة وهندسة الروبوتات, هندسة أجهزة القياس والسيطرة,هندسة خدمات المباني', 'الهندسة الكيميائية', 'هندسة الطاقة', 'الهندسة المدنية ', 'الهندسة الكهربائية, هندسة الحاسوب,هندسة بيئية', 'الهندسة الكيميائيــــــة والبتروكيميائية', ' هندســـــة االلكترونيــــــات واالتصاالت', ' الهندسة المدنية,الهندسة الميكانيكية,هندسة األجهزة وااللكترونيات', 'هندسة الحاسب اآللي في المجاالت اآلتية,- امن المعلومات ', 'كلية الهندسة', 'الهندسة', 'الهندسة', 'الهندسة', 'الهندسة', 'الهندسة', 'الهندسة', 'الهندسة', 'الهندسة', 'الهندسة الميكانيكية', ' التخصصات الهندسية', ' االلكترونيات - الرسم المعماري', ' االلكترونيات - الرسم المعماري', ' االلكترونيات - الرسم المعماري', ' االلكترونيات - الرسم المعماري', 'الطاقة - اإللكترونيات - الميكاترونكس', ' االلكترونيات - الرسم المعماري', 'االلكترونيات']

        h_n_a_both=['جامعة الكويت', 'كلية عمان البحرية الدولية', 'الجامعة الألمانية للتكنولوجيا', 'الجامعة الوطنية للعلوم والتكنولوجيا', 'كلية صور الجامعية', 'جامعة صحار', 'الكلية الدولية للهندسة والإدارة', 'الكلية الوطنية لتقنية السيارات', 'جامعة البريمي', 'جامعة الشرقية', 'جامعة الشرقية', 'جامعة الشرقية', 'جامعة ظفار', 'الكلية العالمية للهندسة والتكنولوجيا', 'جامعة مسقط', 'جامعة مسقط', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'كلية الشرق الأوسط', 'كلية الشرق الأوسط', 'كلية الشرق الأوسط', 'جامعة السلطان قابوس', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعة التقنية والعلوم التطبيقية', 'الجامعات والكليات الخاصة', 'الكلية المهنية بالسيب', 'الكلية المهنية بصحــم', 'الكلية المهنية بصــــور', 'الكلية المهنية بعبـــري', 'الكلية المهنية بشناص', 'الكلية المهنية بالبريمي', 'الكلية المهنية بصاللـــة']


        p_n_a_final=[] 
        h_n_a_final=[]

        code=[]
        code_m=[]
        if gender=="male":
            gen="M"
        else:
            gen="F"
        if pm>=70 and e>=70 and p>=70 and b>=70:
            if avm>=85:
                code.append("SE920")
        if (am>=60 or pm>=60) and e>=55 and p>=60 and c>=60:
            if avm>=65:
                code.append("BS061")
        if (pm>=70) and e>=70 and p>=60 and c>=60:
            if avm>=65:
                code.append("BS209")
        if (am>=65 and pm>=65) and e>=55 and (p>=65 or c>=66):
            if avm>=65:
                code.append("BS051")
        if (pm>=60) and e>=55 and (p>=60 or c>=60):
            if avm>=65:
                code.append("BS295")
                code.append("BS026")
                code.append("BS246")
                code.append("BS056")
    
        if (pm>=60) and e>=55 and (p>=60 or c>=60 or pm>=60):
            if avm>=65:
                code.append("BS226")
                code.append("BS217")
                code.append("BS087")
        if (pm>=60) and e>=55:
            if avm>=65:
                code.append("BS119")
                code.append("BS293")
                code.append("BS010")
        if (pm>=60) and e>=55 and p>=60:
            if avm>=65:
                code.append("BS034")
                code.append("BS266")
                code.append("BS013")

        if (pm>=60) and e>=55 and c>=60:
            if avm>=65:
                code.append("BS291")
        if (pm>=60) and e>=55 and c>=60 and p>=60:
            if avm>=65:
                code.append("BS014")
        if (pm>=60) and e>=55 and p>=65:
            if avm>=65:
                code.append("BS043")
        if (am>=60 or pm>=60) and e>=55:
            if avm>=65:
                code.append("BS046")
        if (pm>=65) and e>=65 and c>=65 and p>=65:
            if avm>=75:
                code.append("SQ200")
        if (pm>=50) and e>=50 and (p>=50 or c>=50):
            if avm>=60:
                code.append("U0101")
                code.append("U0801")
                code.append("U0201")
                code.append("U0301")
                code.append("U0401")
                code.append("U0501")
                code.append("U0601")
                code.append("U0701")
        if (am>=50 or pm>=50) and e>=50 and p>50 and c>=50 and b>=50:
            if avm>=65:
                code.append("PDO001")
        if (pm>=65) and e>=55 and ((c>=65 and p>=65) or (p>=65 and b>=65) or (b>=65 or c>=65)):
            if avm>=65:
                code.append("BS042")

        if (pm>=55) and e>=55 and p>=55:
            if gen=="M":
                if avm>=50:
                    code_m.append("MT001")
                    code_m.append("MT002")
                    code_m.append("MT004")
                    code_m.append("MT005")
    
        if (pm>=60) and e>=60 and p>=60:
            if gen=="M":
                if avm>=50:
                    code_m.append("MT003")
        if (pm>=65) and e>=65 and p>=65:
            if gen=="M":
                if avm>=65:
                    code_m.append("MT009")
        if (pm>=50) and e>=50 and p>=50:
            if gen=="M":
                if avm>=50:
                    code_m.append("VC001")
                    # Automotive Technology
                    code_m.append("VC003")
                    code_m.append("VC006")
                    code_m.append("VC008")
                    code_m.append("VC012")
                    code_m.append("VC015")
            if avm>=50:
                code.append("VC001")
                code.append("VC003")
                code.append("VC006")
                code.append("VC008")
                code.append("VC010")
                code.append("VC015")
                code.append("VC012")
        if (am>=65 or pm>=65) and (p>=65 and ed>=70 and me>=70):
            if avm>=70:
                code.append("U1220")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i]) 
            h_n_a_final.append(h_n_a_both[i])
        if gender=="male":
            p_c_male=['MT001', 'MT002', 'MT003', 'MT004', 'MT005', 'MT009', 'VC001', 'VC003', 'VC006', 'VC008', 'VC012', 'VC015']
            p_n_male=['Systems Engineering,Civil Engineering and Quantity Surveying', 'Systems Engineering,Civil Engineering and Quantity Surveying', 'Aeronautical Engineering,Systems Engineering,Civil Engineering and Quantity Surveying', 'Marine Engineering,Civil Engineering and Quantity Surveying', 'Systems Engineering,Civil Engineering and Quantity Surveying', 'Aeronautical Engineering', 'Automotive Technology - Energy - Mechanics', 'Automotive Technology - Energy - Mechanics', 'Automotive Technology - Energy - Mechanics', 'Energy - Mechanics', 'Automotive Technology - Energy - Mechanics', 'Energy']
            h_n_male=['Military Technological College', 'Military Technological College', 'Military Technological College', 'Military Technological College', 'Military Technological College', 'Military Technological College', 'Seeb Vocational College', 'Saham Vocational College', 'Sur Vocational College', 'Ibri Vocational College', 'Buraimi Vocational College', 'Salalah Vocational College']
            indexes=[]

            p_n_a_m=['هندسة النظم,هندسة مدنية ومسح الكميات', 'هندسة النظم,هندسة مدنية ومسح الكميات', 'هندسة الطيران,هندسة النظم,هندسة مدنية ومسح الكميات', 'هندسة بحرية,هندسة مدنية ومسح الكميات', 'هندسة النظم,هندسة مدنية ومسح الكميات', 'هندسة الطيران', 'تقنية السيارات- الطاقة -الميكانيكا', 'تقنية السيارات- الطاقة -الميكانيكا', 'تقنية السيارات- الطاقة -الميكانيكا', 'الطاقة -الميكانيكا', 'تقنية السيارات- الطاقة -الميكانيكا', 'الطاقة']


            h_n_a_m=['الكلية العسكريـة التقنيـــــــة', 'الكلية العسكريـة التقنيـــــــة', 'الكلية العسكريـة التقنيـــــــة', 'الكلية العسكريـة التقنيـــــــة', 'الكلية العسكريـة التقنيـــــــة', 'الكلية العسكريـة التقنيـــــــة', 'الكلية المهنية بالسيب', 'الكلية المهنية بصحــم', 'الكلية المهنية بصــــور', 'الكلية المهنية بعبـــري', 'الكلية المهنية بالبريمي', 'الكلية المهنية بصاللـــة']

            for i in code_m:
                indexes.append(p_c_male.index(i))
                code_final.append(i)
            for i in indexes:
                p_n_final.append(p_n_male[i])
                h_n_final.append(h_n_male[i])
                p_n_a_final.append(p_n_a_m[i]) 
                h_n_a_final.append(h_n_a_m[i])
        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]

        return final
            
    ################################## Agriculture ###################################

    if major_program=='agriculture':
        
        p_c=['VC026', 'MS004', 'MS005', 'MS006', 'MS007', 'MS008', 'SQ001', 'VC005', 'BS200']
       
       
        p_n=['Fish Training (Fish Quality Control)    ', 'Fish Training (Aquaculture)   ', 'Fish Training (Fish Quality Control)    ', 'Maritime Training (Navigation & Fishing Technology (Navigation of Fishing Vessels)  ', 'Maritime Training (Naval Engineering (marine engines mechanics)      ', 'Water Technology (Water Treatment & Sewage Water Treatment)          ', 'College of Agricultural and Marine Sciences  ', 'Agricultural Training  ', 'Environmental Management and Practice   ']
        
        h_n=['Vocational College Salalah    ', 'Al-Khaborah Vocational College for Marine Sciences', 'Al-Khaborah Vocational College for Marine Sciences', 'Al-Khaborah Vocational College for Marine Sciences', 'Al-Khaborah Vocational College for Marine Sciences', 'Al-Khaborah Vocational College for Marine Sciences', 'Sultan Qaboos University    ', 'Vocational College  Saham', 'Global College of Engineering and Technology']

        code=[]
        p_n_a=['التدريب السمكي (سلامة وضبط جودة الاغذية البحرية)', 'التدريب السمكي/ تربية الأحياء المائية (تربية الأحياء البحرية)', 'التدريب السمكي (سلامة وضبط جودة الاغذية البحرية)', 'التدريب البحري/ تقنيات الملاحة البحرية والصيد (ملاحة سفن الصيد)', 'التدريب البحري/ الهندسة البحرية (ميكانيكا المحركات البحرية)', 'تقنية المياه (معالجة المياه ومياه الصرف الصحي)', 'كلية العلوم الزراعية والبحرية', 'التدريب الزراعي', 'الإدارة والممارسة البيئية ']
        
        
        h_n_a=['الكلية المهنية بصلالة', 'الكلية المهنية للعلوم البحرية بالخابورة', 'الكلية المهنية للعلوم البحرية بالخابورة', 'الكلية المهنية للعلوم البحرية بالخابورة', 'الكلية المهنية للعلوم البحرية بالخابورة', 'الكلية المهنية للعلوم البحرية بالخابورة', 'جامعة السلطان قابوس ', 'الكلية المهنية بصحم', 'الكلية العالمية للهندسة والتكنولوجيا']


        p_n_a_final=[] 
        h_n_a_final=[] 

        if gender=="male":
            gen="M"
        else:
            gen="F"
        if avm>=50:
            #if (pm>=65 or am>=60) and e>=55:
                #code.append("BS200")
            #if (pm>=65) and (e>=65) and ((c>=65 and p>=65) or (p>=65 and b>=65) or (c>=65 and b>=65)):
                #code.append("SQ001")
            if (pm>=50 or am>=50) and (e>=50) and (p>=50 or c>=50 or b>=50):
                code.append("VC005")
                code.append("MS004")
                if gen=="M":
                    code.append("MS006")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
            if (am>=50) and (e>=50):
                code.append("VC026")
                code.append("MS005")
            if (pm>=50) and (e>=50) and (p>=50):
                if gen=="M":
                    code.append("MS007")
            if (pm>=50) and (e>=50) and (p>=50) and (c>=50):
                code.append("MS008")
        if avm>=65:
            if (pm>=65 or am>=60) and e>=55:
                code.append("BS200")
        if avm>=75:
            if (pm>=65) and (e>=65) and ((c>=65 and p>=65) or (p>=65 and b>=65) or (c>=65 and b>=65)):
                code.append("SQ001")

        indexes=[]
        for i in code:
            indexes.append(p_c.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n[i])
            h_n_final.append(h_n[i])
            p_n_a_final.append(p_n_a[i]) 
            h_n_a_final.append(h_n_a[i])
        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]

        return final



    ####################################################################################### Health #########################################################
    if major_program=='health':

        p_c=['SE008', 'SE005', 'SE017', 'SE021', 'SE003', 'SE010', 'SE004', 'SE012', 'SE007', 'SE009', 'SE044', 'SE063', 'SE416', 'SE967', 'SE968', 'SE969', 'BS001', 'BS006', 'BS017', 'BS008', 'BS227', 'BS228', 'BS230', 'BS002', 'BS289', 'BS018', 'BS086', 'BS215', 'BS054', 'SQ050', 'SQ055', 'SQ100', 'U0106', 'PI005', 'IH001', 'IH002', 'IH003', 'NM001', 'NH001', 'NI001', 'NU001', 'NS001', 'NR001', 'NN001', 'NA001', 'HM001', 'PDO015', 'PDO016', 'PDO018', 'PDO019', 'PDO020']
       
        p_n=['Medicine', 'Medicine', 'Medicine', 'Medicine', 'Medicine', 'Medicine', 'Medicine', 'Medicine', 'Medicine', 'Medicine', 'Nursing', 'Respiratory Care (Therapy)', 'Radiation Therapy (Radiotherapy, Diagnostic/Medical Imaging),Radiography,Medical Physics or Physics with Medical Physics,Prosthetics & Orthotics,Sport Rehabilitation,Physiotherapy,Occupational Therapy,Speech & Language Therapy,Dietetics (NOT Nutrition  or MDiet),Podiatry,Paramedic Science,Public Health Promotion,Audiology or Dental Technology', 'Disabilities Studies', 'Natural Therapy', 'Veterinary Medicine', 'Doctor of Medicine', 'Medical and Dental Surgery', 'Nursing', 'Physical Therapy', 'Nursing', 'Optics', 'Science in Occupational Health and Safety', 'Pharmacy', 'Pharmacy', 'Veterinary Medicine', 'Medical Laboratory Sciences', 'Public Health', 'Medical Laboratory Sciences', 'Doctor of Medicine', 'Biomedical Sciences', 'Not Available', 'Pharmacy', 'Bachelor of Pharmacy', 'Bachelor of Medical Laboratory Sciences', 'Bachelor of Medical Imaging', 'Bachelor of Physiotherapy', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Science in Nursing', 'Bachelor of Health Information Management', 'Nursing', 'Nursing', 'Pharmacy', 'Pharmacy', 'Veterinary Medicine']      
        h_n=['University College of Dublin', 'Royal College of Surgeons', 'Trinity College', 'National University of Ireland', 'Arabian Gulf University', 'University of Nicosia', 'Medicine in New Zealand ', 'University of Glasgow', 'University of Aberdeen', 'University of Birmingham', 'University of Louisiana-Lafayette', 'University of Toledo', 'External  Scholarships Department', 'Zaqaziq University', 'Cairo University', 'Cairo University', 'National University of Science and Technology', 'Oman Dental College', 'Nizwa University', 'Nizwa University', 'Al Buraimi University', 'Al Buraimi University', 'Al Buraimi University', 'National University of Science and Technology', 'Nizwa University', "A'Sharqiyah University", "A'Sharqiyah University", "A'Sharqiyah University", 'National University of Science and Technology', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'University of Technology and Applied Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Oman College of Health Sciences', 'Nizwa University', 'Al Buraimi University', 'Nizwa University', 'National University of Science and Technology', "A'Sharqiyah University"]
        h_n_a=['جامعة كلية دبلن', 'الكلية الملكية للجراحين', 'كلية ترينيتي', 'جامعة أيرلندا الوطنية', 'جامعة الخليج العربي', 'جامعة نيقوسيا', 'الطب في نيوزيلندا', 'جامعة جلاسكو', 'جامعة أبردين', 'جامعة برمنجهام', 'جامعة لويزيانا لافاييت', 'جامعة توليدو', 'دائرة الابتعاث الخارجي', 'جامعة الزقازيق', 'جامعة القاهرة', 'جامعة القاهرة', 'الجامعة الوطنية للعلوم والتكنولوجيا', 'كلية عمان لطب الأسنان', 'جامعة نزوى', 'جامعة نزوى', 'جامعة البريمي', 'جامعة البريمي', 'جامعة البريمي', 'الجامعة الوطنية للعلوم والتكنولوجيا', 'جامعة نزوى', 'جامعة الشرقية', 'جامعة الشرقية', 'جامعة الشرقية', 'الجامعة الوطنية للعلوم والتكنولوجيا', 'جامعة السلطان قابوس', 'جامعة السلطان قابوس', 'جامعة السلطان قابوس', 'الجامعة التقنية والعلوم التطبيقية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'كلية عمان للعلوم الصحية', 'جامعة نزوى', 'جامعة البريمي', 'جامعة نزوى', 'الجامعة الوطنية للعلوم والتكنولوجيا', 'جامعة الشرقية']
        p_n_a=['طب', 'طب', 'طب', 'طب', 'طب', 'طب', 'طب', 'طب', 'طب', 'طب', 'التمريض', 'رعاية الجهاز التنفسي (علاج)', 'العلاج الإشعاعي (العلاج الإشعاعي ، التشخيص / التصوير الطبي),التصوير الشعاعي,الفيزياء الطبية أو الفيزياء مع الفيزياء الطبية,الأطراف الصناعية وتقويم العظام,التأهيل الرياضي,العلاج الطبيعي,علاج بالممارسة,علاج النطق واللغة,علم التغذية (ليس التغذية أو النظام الغذائي),علاج الأرجل,علم المسعفين,تعزيز الصحة العامة,السمعيات أو تكنولوجيا طب الأسنان', 'دراسات الإعاقة', 'العلاج الطبيعي', 'طب بيطري', 'طب عام', 'طب وجراحة الفم والأسنان', 'التمريض', 'العلاج الفيزيائي', 'التمريض', 'علم البصريات', 'العلوم في الصحة والسلامة المهنية', 'الصيدلة', 'الصيدلة', 'الطب البيطري', 'علوم المختبرات الطبية', 'الصحة العامة', 'علوم المختبرات الطبية', 'دكتور بالطب', 'العلوم الطبية الحيوية', 'Not Available', 'الصيدلة', 'بكالوريوس صيدلة', 'بكالوريوس علوم المختبرات الطبية', 'بكالوريوس التصوير الطبي', 'بكالوريوس علاج طبيعي', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'بكالوريوس العلوم في التمريض', 'إدارة المعلومات الصحية', 'التمريض', 'التمريض', 'الصيدلة', 'الصيدلة', 'الطب البيطري']

        h_n_a_final=[]  
        p_n_a_final=[]
  
        code=[]
        avm=avm  
        if e>=90 and c>=95 and ((b>=90 and p>=90) or (p>=90 or pm>=90) or (pm>=90 and b>=90)):
            if avm>=90:
                code.append('SE008')
            if avm>=95:
                code.append('SE005')
        if e>=95 and c>=96 and b>=96 and am>=96:
            if avm>=95:
                code.append("SE017")
        if e>=90 and c>=90 and b>=90 and am>=85:
            if avm>=90:
                code.append("SE021")
        if e>=85 and c>=90 and b>=90 and (p>=85 or pm>=85):
            if avm>=95:
                code.append("SE003")
            if avm>=90:
                code.append("SE010")
        if e>=90 and c>=95 and b>=90 and (p>=85 or pm>=85):
            if avm>=90:
                code.append("SE004")
                code.append("SE012")
                code.append("SE007")
        if e>=90 and c>=95 and b>=95 and (p>=85 or pm>=85):
            if avm>=95:
                code.append("SE009")
        if e>=90 and (b>=90 or c>=90) and ss>=75 and (am>=80 or pm>=80):
            if avm>=85:
                code.append("SE044")
                code.append("SE063")
        if e>=85 and ((b>=85 and c>=85 and p>=85) or (c>=85 and p>=85 and pm>=85) or (p>=85 and pm>=85 and b>=85) or (pm>=85 and b>=85 and c>=85)):
            if avm>=85:
                code.append("SE416")
        if e>=80 and c>=80 and b>=80 and p>=80:
            if avm>=85:
                code.append("SE967")
        if e>=85 and c>=85 and b>=85 and p>=85:
            if avm>=90:
                code.append("SE968")
                code.append("SE969")
        if e>=70 and c>=80 and (b>=80 or hs>=80):
            if avm>=80:
                code.append("BS001")
        if e>=80 and b>=80 and (am>=65 or pm>=65):
            if avm>=65:
                code.append("BS006")
        if e>=60 and c>=60 and b>=60:
            if avm>=65:
                code.append("BS017")
                code.append("BS008")
        if e>=60 and c>=60 and (b>=60 or hs>=60) and pm>=60:
            if avm>=65:
                code.append("BS227")    
        if e>=55 and c>=60 and (b>=60 or hs>=60) and pm>=60:
            if avm>=65:
                code.append("BS228")
                code.append("BS230")
        if e>=65 and c>=66 and (b>=65 or hs>=65):
            if avm>=65:
                code.append("BS002")
        if e>=60 and c>=60 and b>=60:
            if avm>=65:
                code.append("BS289")
        if e>=70 and b>=70 and (c>=65 or p>=65):
            if avm>=70:
                code.append("BS018")
        if e>=65 and c>=65 and b>=65:
            if avm>=65:
                code.append("BS086")
            if avm>=70:
                code.append("BS215")
        if e>=65 and c>=65 and (b>=65 or hs>=65):
            if avm>=65:
                code.append("BS054")
        if e>=80 and ((c>=80 and p>=80) or (p>=80 and b>=80) or (b>=80 and c>=80)):
            if avm>=85:
                code.append("SQ050")
                code.append("SQ055")
        if e>=65 and ((b>=65 and c>=65 and p>=65) or (c>=65 and p>=65 and pm>=65) or (p>=65 and pm>=65 and b>=65) or (pm>=65 and b>=65 and c>=65)):
            if avm>=85:
                code.append("SQ100")
        
        if e>=50 and c>=50 and (b>=50 or hs>=50) and p>=60:

            if avm>=60:

                code.append("U0106")
        if c>=65 and (b>=65 or hs>=65):
            if avm>=65:
                code.append("PI005")
                code.append("IH001")
        if p>=65 and (b>=65 or hs>=65):
            if avm>=65:
                code.append("IH002")
                code.append("IH003")
        if c>=60 and (b>=60 or hs>=60):
            if avm>=65:
                code.append("NM001")
                code.append("NH001")
                code.append("NI001")
                code.append("NU001")
                code.append("NS001")
                code.append("NR001")
                code.append("NN001")
                code.append("NA001")
        if (b>=65 or hs>=65) and (am>=65 or pm>=65):
            if avm>=65:
                code.append("HM001")
        if e>=60 and c>=60 and b>=60:
            if avm>=65:
                code.append("PDO015")
        if e>=60 and c>=60 and (b>=60 or hs>=60) and pm>=60:
            if avm>=65:
                code.append("PDO016")
        if e>=60 and c>=60 and b>=60:
            if avm>=65:
                code.append("PDO018")
        if e>=65 and c>=65 and (b>=65 or hs>=65):
            if avm>=65:
                code.append("PDO019")
        if e>=70 and b>=70 and (c>=65 or p>=65):
            if avm>=70:
                code.append("PDO020")
        indexes=[]
        for i in code:
            indexes.append(p_c.index(i))
        code_final=code
        p_n_final=[]

        h_n_final=[]
    
        for i in indexes:
            print(i)
            p_n_final.append(p_n[i])
            h_n_final.append(h_n[i])
            p_n_a_final.append(p_n_a[i])  
            h_n_a_final.append(h_n_a[i])
        final=[]

        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final



    #####################################################################################  Creative Arts  ##################################################
    if major_program=='creative_arts':
        p_c_both=['BS196', 'DS004', 'SF004', 'BS265', 'BS136', 'BS137', 'BS139', 'BS276', 'SQ780', 'BS286', 'U0107', 'U0204', 'U0210', 'U0404', 'U0904']
        p_n_both=['Journalism -Public Relations -Broadcasting -Advertising -Visual Communication Design', 'ART', 'ART', 'Design Specialties (Mobility Disability)', 'Digital Graphic Design -Animation -Photography', 'Fine arts', 'Fashion design', 'Graphic Design and Interior Design (Hearing and Speech Impairments)', 'College of Arts and Social Sciences (Music and Musical Sciences)', 'Fine arts', 'Diploma Photography (Muscat)', 'Mass Communication (Nizwa)', 'Design (Nizwa)', 'Mass Communication (Salalah)', 'Mass Communication (Sur)']    
        h_n_both=['Bayan College', 'Bayan College', 'Bayan College', 'Private Universities and Colleges', 'Scientific College of Design', 'Scientific College of Design', 'Scientific College of Design', 'Scientific College of Design', 'Sultan Qaboos University', 'University  of Nizwa', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences']
        
        p_n_a_both=['-الصحافة -العلاقات العامة والاتصال -الإذاعة والتلفزيون -الإعلان -تصميم الإتصال المرئي', 'الفنون الإبداعية', 'مختلف تخصصات الفنون الإبداعية حسب ما تقدمة كل مؤسسة تعليمية خاصة لمؤهل الدبلوم', 'تخصصات التصميم (إعاقة حركية)', '-التصميم الجرافيكي الرقمي  - الرسوم المتحركة - التصوير الفوتوجرافي', 'الفنون الجميلة', 'تصميم الأزياء', 'التصميم الجرافيكي والتصميم الداخلي (إعاقات سمعية ونطقية)', 'كلية الآداب والعلوم الاجتماعية (الموسيقى والعلوم الموسيقية)', 'الفنون الجميلة', 'دبلوم التصوير الضوئي (مسقط)', ' الإتصال الجماهيري (نزوى)', 'التصميم (نزوى)', ' الإتصال الجماهيري (صلالة)', ' الإتصال الجماهيري (صور)']

        h_n_a_both=['كلية البيان', 'كلية البيان', 'كلية البيان', 'الجامعات والكليات الخاصة ', 'الكلية العلمية للتصميم', 'الكلية العلمية للتصميم', 'الكلية العلمية للتصميم', 'الكلية العلمية للتصميم', 'جامعة السلطان قابوس ', 'جامعة نزوى', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ']



        p_n_a_final=[]
        h_n_a_final=[]


        
        code=[]
        code_f=[]
        avm=avm 
        if gender=="male":
            gen="M"
        else:
            gen="F"
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS196")
        if e>=55 and (am>=55 or pm>=55):
            if avm>=60:
                code.append("DS004")
                code.append("SF004")
        if e>=55:
            if avm>=65:
                code.append("BS136")
                code.append("BS139")
        if e>=65 and p>=65 and (am>=65 or pm>=65):
            if avm>=75:
                code.append("SQ780")
        if e>=50 and (am>=50 and pm>=50):
            if avm>=60:
                code.append("U0107")
                code.append("U0210")
        if e>=50:
            if gen=='F' and avm>=60:
                code_f.append("U0108")
            if avm>=60:
                code.append("U0204")
                code.append("U0404")
                code.append("U0904")
        if e>=60 and (am>=60 or pm>=60):
            if gen=="F" and avm>=65:
                code_f.append("BS108")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i])  
            h_n_a_final.append(h_n_a_both[i])
        if gen=="F":
            p_c_f=['U0108', 'BS108']
            p_n_f=['Fashion Design (Muscat)', 'Graphic Design']
            h_n_f=['University of Technology and Applied Sciences', 'Al Zahra College for Women']
            p_n_a_f=['دبلوم تصميم الأزياء - للاناث (مسقط)', 'تصميم غرافيك']
            h_n_a_f=['جامعة التقنية والعلوم التطبيقية ', 'كلية الزهراء للبنات']



            indexes=[]
            for i in code_f:
                indexes.append(p_c_f.index(i))
                code_final.append(i)
            for i in indexes:
                p_n_final.append(p_n_f[i])
                h_n_final.append(h_n_f[i])
                p_n_a_final.append(p_n_a_f[i])  
                h_n_a_final.append(h_n_a_f[i])
        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final
    ######################################################################################  Information Technology  ############################################################################################
    if major_program=="information_technology":
        p_c_both=['BS237', 'BS084', 'BS089', 'BS076', 'BS234', 'BS035', 'BS257', 'BS268', 'BS210', 'BS206', 'BS212', 'BS148', 'BS044', 'BS187', 'BS094', 'BS178', 'BS179', 'BS261', 'DS002', 'DS010', 'SF002', 'SP002', 'BS027', 'BS287', 'U0098', 'U0102', 'U0202', 'U0302', 'U0402', 'U0502', 'U0602', 'U0702', 'U0802', 'U0902', 'BS206', 'BS210', 'BS212', 'BS118', 'BS126', 'BS032']
        
        p_n_both=['Information Technology and Computing - Computing and Business Management - Computer Science -Networking and Data Security', 'Management Information Systems', 'Internet and information technology-Cybersecurity', 'Software Engineering -Information Systems -Computer Sciences', 'Artificial Intelligence', 'Computer Science', 'Computing science -Mobile Computing  -Information Systems -Computer Science (Artificial Intelligent) -Computer Science (Data Analytics)', 'Computer Science', 'Bachelor of Science in Cyber Security', 'Computer Science', 'Artificial Intelligence', 'Computer Science', 'Software Technology -Computing and Information Systems -Computer Science -Database Management Systems', 'Computer and Internet Applications -Networking -Computing (Oil and Gas pathway) -Computing (Software Engineering pathway) -Computing (Banking Information Systems pathway)', 'Computer Science(Artificial Intelligence-Cybersecurity-Data Science-Mobile Applications)-Information Security-Information Systems-Applied Techniques(Internet of Things-Data Analysis-Augmented and Virtual Reality-Robotics and intelligent Systems)', 'Management Information Systems', 'Computer Science', 'Specialization in Information Technology ', 'تخصصات تكنولوجيا المعلومات', 'Information Technology', 'Information Technology', 'Information Technology', 'Computing and Multimedia  \tComputinComputing and Multimedia -Computing and Web Engineering -Networking & Database -Business Administration (Information Technology) -Software engineering', 'Web Design & Information Security -Computer Science -Information Systems', 'Information Technology', 'Information Technology (Muscat)', 'Information Technology (Nizwa)', 'Information Technology (Ibra)', 'Information Technology (Salalah)', 'Information Technology (Almusanaah)', 'Information Technology (Shinas)', 'Information Technology (Ibri)', 'Information Technology (Suhar)', 'Information Technology (Sur)', 'Computer Science', 'Cyber Security', 'Artificial Intelligence', 'Information Technology', 'Computer Science, Information Science or Management Information Systems', 'Management Information Systems']
        
        h_n_both=['Arab Open University', 'Al Sharqiyah University', 'Al Sharqiyah University', 'Al- Buraimi College', 'Buraimi University', 'Dhofar University', 'Gulf College', 'Global College of Engineering and Technology', 'German University of Technology', 'German University of Technology', 'German University of Technology', 'Muscat College', 'Middle East College', 'Majan College', 'Modern College of Business and Science', 'Oman College of  Management and Technology', 'Oman College of  Management and Technology', 'Private Universities and Colleges', 'Private Universities and Colleges', 'Private Universities and Colleges', 'Private Universities and Colleges', 'Private Universities and Colleges', 'Sohar  University', 'University  of Nizwa', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'German University of Technology,(Data Not Mentioned)', 'German University of Technology,(Data Not Mentioned)', 'German University of Technology,(Data Not Mentioned)', 'Sur University College,(Data Not Mentioned)', 'Mazoon College', 'Dhofar University']
        
        p_n_a_both=['تقنية المعلومات والحوسبة -الحوسبة وإدارة الاعمال-علوم الحاسوب-الشبكات وأمن البيانات', 'نظم المعلومات الادارية ', 'الانترنت وتقنية المعلومات - الامن السبراني', '-هندسة البرمجيات -أنظمة المعلومات -علوم الحاسب الألي', 'الذكاء الاصطناعي', 'علوم الكمبيوتر', 'علوم الحاسوب -الحوسبة المتنقلة -الذكاء الصناعي -تحليل البيانات -نظم المعلومات الادارية', 'علوم الكمبيوتر', 'العلوم في الأمن السيبراني', 'علوم الكمبيوتر', 'الذكاء الاصطناعي', 'علوم الكمبيوتر', '-تقنية البرمجيات -علوم الحاسب الآلي -تحليل البيانات', 'الحاسوب وتطبيقات الإنترنت  -الشبكات  -الحوسبة (النفط والغاز) -الحوسبة (هندسة البرمجيات) -الحوسبة (نظم المعلومات المصرفية)', 'علوم الحاسوب(الذكاء الاصطناعي-الامن السيبراني-علم البيانات-تطبيقات الهواتف المحمولة)نظم المعلومات-أمن المعلومات-التقنيات التطبيقية(انترنت الأشياء-تحليل البيانات-الوقع المعزز والافتراضي-الروبوت والأنظمة الذكية)', 'نظم المعلومات الادارية ', 'علوم الكمبيوتر', 'تخصصات تكنولوجيا المعلومات (إعاقة حركية)', 'تخصصات تكنولوجيا المعلومات', 'تخصصات تكنولوجيا المعلومات', 'مختلف تخصصات تكنولوجيا المعلومات حسب ما تقدمه كل مؤسسة تعليمية خاصة لمؤهل الدبلوم', 'مختلف تخصصات تكنولوجيا المعلومات حسب ما تقدمه كل مؤسسة تعليمية خاصة لمؤهل الدبلوم', '-علوم الحاسوب والوسائط المتعددة -علوم الحاسوب وهندسة الويب -الشبكات وقاعدة البيانات -نظم المعلومات الإدارية -هندسة البرمجيات ', '-تصميم الويب وأمن المعلومات -علوم الحاسوب -نظم المعلومات', 'تخصصات تكنولوجيا المعلومات', 'تقنية المعلومات (مسقط)', 'تقنية المعلومات (نزوى)', 'تقنية المعلومات (ابراء)', 'تقنية المعلومات (صلالة)', 'تقنية المعلومات (المصنعة)', 'تقنية المعلومات (شناص)', 'تقنية المعلومات (عبري)', 'تقنية المعلومات (صحار)', 'تقنية المعلومات (صور)', 'علوم الكمبيوتر', 'الأمن الإلكتروني', 'الذكاء الاصطناعي', 'تخصصات تكنولوجيا المعلومات', 'علوم الكمبيوتر أو علوم المعلومات أو نظم المعلومات الإدارية', 'نظم المعلومات الادارية ']

        h_n_a_both=[' الجامعة العربية المفتوحة', 'جامعة الشرقية', 'جامعة الشرقية', 'كلية البريمي', ' العمارة الداخلية -الهندسة المعمارية', 'جامعة ظفار', 'كلية الخليج', 'الكلية العالمية للهندسة والتكنولوجيا', 'الجامعة الألمانية للتكنولوجيا', 'الجامعة الألمانية للتكنولوجيا', 'الجامعة الألمانية للتكنولوجيا', 'كلية مسقط', 'كلية الشرق الأوسط', 'كلية مجان', 'الكلية الحديثة للتجارة والعلوم', 'كلية عمان للإدارة والتكنولوجيا', 'كلية عمان للإدارة والتكنولوجيا', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'جامعة صحار', 'جامعة نزوى', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'الجامعة الألمانية للتكنولوجيا', 'الجامعة الألمانية للتكنولوجيا', 'الجامعة الألمانية للتكنولوجيا', 'كلية صور الجامعية', 'كلية مزون', 'جامعة ظفار']

        p_n_a_final=[] 
        
        h_n_a_final=[] 
        
        
        code=[]
        avm=avm 
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS237")
                code.append("BS084")
                code.append("BS076")
                code.append("BS257")
                code.append("BS268")
        if e>=65 and pm>=65:
            if avm>=65:
                code.append("BS089")
        if e>=55 and p>=60 and pm>=60:
            if avm>=65:
                code.append("BS234")
                code.append("BS035")
        if e>=70 and pm>=65:
            if avm>=65:
                code.append("BS210")
                code.append("BS206")
                code.append("BS212")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS148")
                code.append("BS044")
                code.append("BS187")
                code.append("BS094")
                code.append("BS178")
                code.append("BS027")
                code.append("BS287")
                code.append("BS118")
                code.append("BS126")
                code.append("BS032")
        if e>=55 and pm>=60:
            if avm>=65:
                code.append("BS179")
        if e>=55 and (am>=55 or pm>=55):
            if avm>=60:
                code.append("BS261")
                code.append("DS002")
                code.append("SF002")
                code.append("SP002")
            if avm>=55:
                code.append("DS010")
        if e>=50 and pm>=50:
            if avm>=60:
                code.append("U0098")
                code.append("U0102")
                code.append("U0202")
                code.append("U0302")
                code.append("U0402")
                code.append("U0502")
                code.append("U0602")
                code.append("U0702")
                code.append("U0802")
                code.append("U0902")
        if e>=70 and pm>=65:
            if avm>=65:
                code.append("BS206")
                code.append("BS210")
                code.append("BS212")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i])  
            h_n_a_final.append(h_n_a_both[i])


        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final
        


    #############################################################################################  Management and Commerce #############################################################################################

    if major_program=="management_and_commerce":
        p_c_both=['BS236', 'BS216', 'BS071', 'BS097', 'BS229', 'BS233', 'BS031', 'VC016', 'BS249', 'BS256', 'BS211', 'BS063', 'BS149', 'BS041', 'BS186', 'BS083', 'BS091', 'BS290', 'BS177', 'BS260', 'DS003', 'DS011', 'SP003', 'SE921', 'SQ250', 'BS024', 'BS168', 'BS012', 'U0099', 'U0103', 'U0203', 'U0303', 'U0403', 'U0503', 'U0603', 'U0703', 'VC014', 'VC004', 'VC009', 'VC011', 'VC002', 'VC007']
        p_n_both=['Management in: -Economics  -Accounting  -Marketing  -Systems -Science in Accounting', 'Team Entrepreneurship -Management -Finance and Accounting.', 'Banking and Finance -Human Resources Development -International Business -Marketing -Business Administration -Accounting', 'Accounting, auditing and finance -\tBanking and Finance -\tBanking and Finance (Islamic Finance) -\tBusiness administration in the following areas: -\tAdministration -\tMarketing -\tHuman Resources -\tLogistics and Supply Chain Management', 'Business Administration with a focus on E-Marketing and Social Media -Management Information Systems -Islamic Banking and Finance -Global Supplies Chain Management and Logistics -Business Administration and E-Business', 'Human Resource Managment ', 'Logistics and Supply Chain Management -Management -Accounting -Finance -Marketing', 'Commercial Studies', 'Fire Safety Management -Health, Safety and Environmental Management -Construction Project Management', 'Business Management Studies -Marketing Management -Business Economics -Accounting & Finance -Business Information Systems', 'International Business and Service Management -Science in Logistics', 'Navigation (Deck officer) -Logistics and Transport Management', 'Project Management', 'Logistics Management -Business Administration with pathway in Marketing -Business Administration with pathway Accounting and Finance -Business Administration with pathway in Human Resource Management -Business Administration with pathway in Human General Management', 'Business Administration -Business Administration (Human Resources Management Pathway)  -Business Administration (Accounting Pathway)  -Business Administration (Information Systems Pathway)  -Business Administration (Marketing Pathway)  -Business Administration (Small Business Pathway)  -Business Administration (Tourism and Events Management Pathway)  -Islamic Banking and Finance -Accounting  -Marketing  -Finance  -EBusiness', 'Accounting-Business Administration(Accounting-Financial-Accounting and Finance-Management Information Systems-Marketing-Management and Career Behavior)-Aviation Management-Airport Management-Aviation Management-Health and Safety Management-Risk Management and Insurance-Transport and Logistics-Design, Creativity and Entrepreneurship Management  Literature in Economics', 'Public Administration -Business Administration (Accounting, Human resources, Management)', 'Logistics and Supply Chain Management - Logistics and transportation management -Accounting and Finance -Business and Management -Marketing ', 'Marketing and Electronic Commerce - Business Administration - Accounting -Banking and Finance', 'Administrative specializations (Mobility disabilities)', 'Management and commercial transactions', 'Business Administration', 'Various majors in management and commercial transactions, according to what each private educational institution offers for the diploma qualification', 'Management Sciences', 'College of Economics and Political Sciences', 'Accounting -Management -Marketing -Business Administration (Information Technology) -Business and Commercial Law', 'Tourism & Hospitality Management  -Events Management  -Tourism Marketing  -Business Enterprise (Service management Pathway)  -Business Enterprise (Innovation and Entrepreneurship Pathway)', 'Tourism and Recreational Management -International Trade and Finance -Business Administration -Accounting -Marketing -Operations Management -Economics and Finance', 'Business Administration / Business Studies', 'Business Studies (Muscat)', 'Business Studies (Nizwa)', 'Business Studies (Ibra)', 'Business Studies (Salalah)', 'Business Studies (Almusanaah)', 'Business Studies (Shinas)', 'Business Studies (Ibri)', 'Commercial Studies', 'Commercial Studies', 'Commercial Studies', 'Commercial Studies', 'Commercial Studies', 'Commercial Studies']
        h_n_both=['Arab Open University', 'Al Sharqiyah University', 'Al- Buraimi College', 'College of Banking and Financial Studies', 'Buraimi University', 'Buraimi University', 'Dhofar University', 'Vocational College Salalah', 'International College of Engineering & Management', 'Gulf College', 'German University of Technology', 'International Maritime College Oman', 'Muscat College', 'Middle East College', 'Majan College', 'Modern College of Business and Science', 'Modern College of Business and Science', 'Muscat University', 'Oman College of  Management and Technology', 'Private Universities and Colleges', 'Private Universities and Colleges', 'Private Universities and Colleges', 'Private Universities and Colleges', 'External  Scholarships Department', 'Sultan Qaboos University', 'Sohar  University', 'Oman Tourism College  ', 'University  of Nizwa', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'Vocational College Burami', 'Vocational College  Saham', 'Vocational College  Ibri', 'Vocational College Shnas', 'Vocational College Seeb', 'Vocational College Sur'] 



        p_n_a_both=['اداره الاعمال في : -المحاسبة -الإدارة -التسويق  -الأنظمة -الاقتصاد -العلوم في المحاسبة', 'ريادة الاعمال الجماعية -التمويل والمحاسبة  - الإدارة ', '-العلوم المالية والمصرفية -تنمية الموارد البشرية -التجارة الدولية -التسويق -إدارة الأعمال -المحاسبة ', 'المحاسبة والتدقيق والمالية -الصيرفة والمالية -الصيرفة والمالية (المالية الإسلامية) -ادارة الاعمال في المجالات الآتية: -الإدارة -التسويق -الموارد البشرية -اللوجستيات وإدارة سلسلة التوريد', 'ادارة الاعمال مع التركيز على التسويق الالكتروني ووسائل التواصل الاجتماعي -إدارة نظم المعلومات - الصيرفة الاسلامية و المالية - إدارة التوريدات العالمية واللوجستية -إدارة الأعمال والأعمال الإلكترونية', 'إدارة الموارد البشرية', '-اللوجستيات وإدارة سلسلة التوريد -الإدارة -المالية -المحاسبة -التسويق', 'الدراسات التجارية', '-إدارة السلامة من الحرائق -إدارة الصحة والسلامة والبيئة -إدارة مشاريع البناء', '-إدارة التسويق -دراسات الأعمال الإدارية -إقتصاديات الأعمال -المحاسبة والمالية', ' إدارة الأعمال الدولية والخدمات  - الخدمات اللوجستية ', 'الملاحة البحرية (ضابط سطح) -إدارة اللوجستيات والنقل', 'إدارة المشاريع', '-الإدارة اللوجستية -إدارة الأعمال (مساق الموارد البشرية) -إدارة الأعمال (مساق المحاسبة والمالية) -إدارة الأعمال (مساق الإدارة العامة) -إدارة الأعمال (مساق التسويق)', '-إدارة الأعمال -إدارة الأعمال (إدارة الموارد البشرية)   -إدارة الأعمال (المحاسبة)  -إدارة الأعمال (نظم المعلومات)  -إدارة الأعمال (التسويق)  -ادارة الأعمال (المشاريع الصغيرة) -إدارة الأعمال (السياحة وإدارة الفعاليات)  -إدارة الأعمال (إدارة عمليات النقل)  -الصيرفة الإسلامية والتمويل -المحاسبة  -التسويق  -المالية  -التجارة الالكترونية', 'المحاسبة-ادارة الاعمال(المحاسبة-المالية-المحاسبة والمالية-انظمة المعلومات الادارية-التسويق-الادارة والسلوك الوظيفي-الادارة والسلوك الوظيفي)-ادارة المطارات-ادارة الطيران-ادارة الصحة والسلامة-ادارة المخاطر والتأمين-ادارة النقل والخدمات اللوجستية-ادارة التصميم والابداع وريادة الاعمال', 'الإدارة العامة - إدارة الاعمال ( المحاسبة، الموارد البشرية، الإدارة)', '-الخدمات اللوجستية وإدارة سلسلة التموين -الخدمات اللوجستية وإدارة النقل -المحاسبة والمالية -الاعمال والاداره -التسويق', '-التسويق والتجارة الإلكترونية -إدارة الأعمال -المحاسبة -العلوم المالية والمصرفية', 'التخصصات الإدارية ( إعاقات حركية )', 'الإدارة والمعاملات التجارية ', 'الإدارة والمعاملات التجارية', 'مختلف التخصصات الإدارة والمعاملات التجارية حسب ما تقدمة كل مؤسسة تعليمية خاصة لمؤهل الدبلوم', 'العلوم الإدارية', 'كلية الإقتصاد والعلوم السياسية', 'المحاسبة -الإدارة -التسويق -إدارة الأعمال (تقنية المعلومات) -الأعمال والقانون التجاري', 'إدارة السياحة والضيافة -إدارة الفعاليات -التسويق السياحي - إدارة الأعمال التجارية ( مسار إدارة الخدمات) - إدارة الأعمال التجارية ( مسار الابتكار وريادة الأعمال)', 'إدارة المشاريع الترفيهية -التجارة الدولية والمالية -إدارة الأعمال -المحاسبة -التسويق -إدارة العمليات -الإقتصاد والمالية', 'إدارة الأعمال / الدراسات التجارية', 'إدارة الأعمال /  الدراسات تجارية (مسقط)', 'إدارة الأعمال /  الدراسات تجارية (نزوى)', 'إدارة الأعمال /  الدراسات تجارية (ابراء)', 'إدارة الأعمال /  الدراسات تجارية (صلالة)', 'إدارة الأعمال /  الدراسات تجارية (المصنعة)', 'إدارة الأعمال /  الدراسات تجارية (شناص)', 'إدارة الأعمال /  الدراسات تجارية (عبري)', 'الدراسات التجارية (البيع التخصصي والتسويق).', 'الدراسات التجارية', 'الدراسات التجارية', 'الدراسات التجارية', 'الدراسات التجارية', 'الدراسات التجارية'] 


        h_n_a_both=[' الجامعة العربية المفتوحة', 'جامعة الشرقية', 'كلية البريمي', 'كلية الدراسات المالية والمصرفية ', ' العمارة الداخلية -الهندسة المعمارية', ' العمارة الداخلية -الهندسة المعمارية', 'جامعة ظفار', 'الكلية المهنية بصلالة', 'كلية الدولية للهندسة والإدارة ', 'كلية الخليج', 'الجامعة الألمانية للتكنولوجيا', 'كلية عمان البحرية الدولية', 'كلية مسقط', 'كلية الشرق الأوسط', 'كلية مجان', 'الكلية الحديثة للتجارة والعلوم', 'الكلية الحديثة للتجارة والعلوم', 'جامعة مسقط', 'كلية عمان للإدارة والتكنولوجيا', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'دائرة البعثات الخارجية', 'جامعة السلطان قابوس ', 'جامعة صحار', 'كلية عمان للسياحة', 'جامعة نزوى', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'الكلية المهنية بالبريمي', 'الكلية المهنية بصحم', 'الكلية المهنية بعبري', 'الكلية المهنية بشناص', 'الكلية المهنية بالسيب', 'الكلية المهنية بصور']



        p_n_a_final=[] 
        h_n_a_final=[] 

        
        avm=avm 
        code=[]
        ba=hs
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS236")
                code.append("BS216")
                code.append("BS071")
                code.append("BS097")
                code.append("BS229")
                code.append("BS233")
                code.append("BS031")
                code.append("BS249")
                code.append("BS256")
                code.append("BS063")
                code.append("BS149")
                code.append("BS041")
                code.append("BS186")
                code.append("BS083")
                code.append("BS091")
                code.append("BS290")
                code.append("BS177")
        if e>=70 and (am>=65 or pm>=60):
            if avm>=65:
                code.append("BS211")
        if e>=55 and (am>=55 or pm>=55):
            if avm>=60:
                code.append("BS260")
                code.append("DS003")
                code.append("SP003")
            if avm>=55:
                code.append("DS011")
        if e>=70 and (am>=70 or pm>=70) and ar>=70:
            if avm>=85:
                code.append("SE921")
        if e>=65 and (am>=80 or pm>=70):
            if avm>=75:
                code.append("SQ250")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS024")
                code.append("BS168")
                code.append("BS012")
        if e>=50 and (am>=50 and pm>=50) and (ss>=50 or ba>=50):
            if avm>=60:
                code.append("U0099")
                code.append("U0103")
                code.append("U0203")
                code.append("U0303")
                code.append("U0403")
                code.append("U0503")
                code.append("U0603")
                code.append("U0703")
        if e>=50 and (am>=50 or pm>=50):
            if avm>=50:
                code.append("VC014")
                code.append("VC004")
                code.append("VC009")
                code.append("VC011")
                code.append("VC002")
                code.append("VC007")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i]) 
            h_n_a_final.append(h_n_a_both[i])
        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final



    ##########################################################################################  Architecture #############################################################


    if major_program=="architecture":
        p_c_both=['BS088', 'BS220', 'BS232', 'VC024', 'BS248', 'BS019', 'BS207', 'BS045', 'BS176', 'SP001', 'BS138', 'BS140', 'BS015', 'BS225', 'VC021', 'VC023', 'VC020', 'VC022', 'BS037', 'BS053', 'BS112', 'BS117']
        p_n_both=['Quantatity Surveying and Commercial management', 'Construction Project Management', 'Interior Architecture -Architectural Engineering', 'Interior Design', 'Facility Management - Construction Project Management', 'Urban and Regional Planning - Architectural Technology and Design', ' Urban Planning and Architectural Design', 'Quantity Surveying and Construction Management', 'Interior Design', 'Dfrent specialities architecture construction for diploma specialization', 'Interior Design', 'Architecture', 'Interior Design and Decoration', 'Architecture', 'International Maritime College Oman', 'Interior Design', 'Interior Design', 'Interior Design', 'Architecture Engineering or Interior Architecture', 'Quantity Surveying and Cost Management', 'Interior Design', 'Architecture Engineering ']
        h_n_both=['Al Sharqiyah University', 'Al Sharqiyah University', 'Buraimi University', 'Vocational College Salalah', 'International College of Engineering & Management', 'Global College of Engineering and Technology', 'German University of Technology in Oman', 'Middle East College', 'Oman College of  Management and Technology', 'Private Universities and Colleges', 'Scientific College of Design', 'Scientific College of Design', 'University  of Nizwa', 'University  of Nizwa', 'Vocational College  Saham', 'Vocational College  Ibri', 'Vocational College Seeb', 'Vocational College Sur', 'Dhofar University ', 'National University of Science & Technology', 'Al Zahra College for Women', 'SUR University College']
       
        p_n_a_both=['حساب الكميات وإدارة الاعمال ', 'إدارة المشاريع الإنشائية', 'العمارة الداخلية -الهندسة المعمارية', 'التصميم الداخلي', 'إدارة المنشأت', 'التخطيط الحضري والإقليمي-التكنولوجيا المعمارية والتصميم', ' تخطيط المدن والتصميم المعماري', 'مسح الكميات وإدارة الإنشاءات', 'التصميم الداخلي', 'مختلف تخصصات العمارة والإنشاء لتخصصات الدبلوم ', 'التصميم الداخلي', 'العمارة', 'هندسة التصميم الداخلي والديكور ', 'العمارة', 'كلية عمان البحرية الدولية', 'التصميم الداخلي', 'التصميم الداخلي', 'التصميم الداخلي', 'هندسة العمارة أو العمارة الداخلية', 'مسح الكميات وإدارة التكاليف', 'التصميم الداخلي', 'الهندسة المعمارية']
        h_n_a_both=['جامعة الشرقية', 'جامعة الشرقية', ' العمارة الداخلية -الهندسة المعمارية', 'الكلية المهنية بصلالة', 'كلية الدولية للهندسة والإدارة ', 'الكلية العالمية للهندسة والتكنولوجيا ', 'الجامعة الألمانية للتكنولوجيا في عمان', 'كلية الشرق الأوسط ', 'كلية عمان للإدارة والتكنولوجيا', 'الجامعات والكليات الخاصة ', 'الكلية العلمية للتصميم', 'الكلية العلمية للتصميم', 'جامعة نزوى', 'جامعة نزوى', 'الكلية المهنية بصحم', 'الكلية المهنية بعبري', 'الكلية المهنية بالسيب', 'الكلية المهنية بصور', 'جامعة ظفار', 'الجامعة الوطنية للعلوم والتكنولوجيا', 'كلية الزهراء للبنات', 'كلية صور الجامعة']


        
        p_n_a_final=[]  
        h_n_a_final=[]
        
        
        if gender=="male":
            gen="M"
        else:
            gen="F"

        code=[]
        code_f=[]
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS088")
        if e>=55 and p>=60 and pm>=60:
            if avm>=65:
                code.append("BS220")
                code.append("BS232")
        if e>=50 and (am>=50 or pm>=50):
            if avm>=50:
                code.append("VC024")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS248")
                code.append("BS019")
        if e>=65 and (pm>=65 or am>=65):
            if avm>=65:
                code.append("BS207")
        if e>=55 and p>=60 and pm>=65:
            if avm>=65:
                code.append("BS045")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS176")
        if e>=55 and p>=55 and (am>=55 or pm>=55):
            if avm>=60:
                code.append("SP001")
        if e>=55:
            if avm>=65:
                code.append("BS138")
        if e>=55 and p>=60 and pm>=60:
            if avm>=65:
                code.append("BS140")
        if e>=55 and pm>=55:
            if avm>=65:
                code.append("BS015")
                code.append("BS225")
        if e>=50 and (am>=50 or pm>=50):
            if avm>=avm_pass:
                code.append("VC021")
                code.append("VC023")
                code.append("VC020")
                code.append("VC022")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS037")
        if e>=55 and (p>=65 or c>=65) and (pm>=65 or am>=65):
            if avm>=65:
                code.append("BS053")
        if e>=60 and (am>=60 or pm>=60):
            if gen=="F" and avm>=65:
                code_f.append("BS112")
        if e>=55 and (p>=60 or c>=60) and am>=60:
            if avm>=65:
                code.append("BS117")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i])  
            h_n_a_final.append(h_n_a_both[i]) 


        if gen=="F":
            p_c_f=['BS112']
            p_n_f=['Interior Design']
            h_n_f=['Al Zahra College for Women']

            p_n_a_f=['التصميم الداخلي']
            h_n_a_f=['كلية الزهراء للبنات']

            indexes=[]
            for i in code_f:
                indexes.append(p_c_f.index(i))
                code_final.append(i)
            for i in indexes:
                p_n_final.append(p_n_f[i])
                h_n_final.append(h_n_f[i]) 
                p_n_a_final.append(p_n_a_f[i]) 
                h_n_a_final.append(h_n_a_f[i])


        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final
    ######################################################################################   Natural and Physical Sciences   ######################################

    if major_program=="natural_physical_sciences":
        p_c_both=['BS085', 'BS224', 'BS208', 'BS090', 'SE922', 'SQ150', 'BS020', 'U0105', 'U0909']
        p_n_both=['Industrial chemistry', 'Human nutrition applied and therapeutic', 'Science in Applied Geoscience', ' Statistics', ' Statistics', 'College of Science', 'Statistics', 'Applied Sciences (Muscat)', 'Applied Biotechnology (Sur)']
        h_n_both=['Al Sharqiyah University', 'Al Sharqiyah University', 'German University of Technology in Oman', 'Modern College of Business and Science', 'External  Scholarships Department', 'Sultan Qaboos University', 'University  of Nizwa', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences']
       
       
        p_n_a_both=['الكيمياء الصناعية', 'تغذية الإنسان التطبيقية والعلاجية', 'علوم الارض التطبيقية', 'الاحصاء', 'الاحصاء', 'كلية العلوم', 'الإحصاء', 'علوم تطبيقية (مسقط)', 'التقنية الحيوية التطبيقية (صور)']
        h_n_a_both=['جامعة الشرقية', 'جامعة الشرقية', 'الجامعة الألمانية للتكنولوجيا في عمان', 'الكلية الحديثة للتجارة والعلوم', 'دائرة البعثات الخارجية', 'جامعة السلطان قابوس ', 'جامعة نزوى', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ']

        p_n_a_final=[]
        h_n_a_final=[]
        
        
        if gender=="male":
            gen="M"
        else:
            gen="F"

        code=[]
        if e>=70 and pm>=70 and (c>=70 or p>=70):
            if avm>=65:
                code.append("BS085")
                code.append("BS224")
        if e>=70 and pm>=70 and c>=60 and p>=60:
            if avm>=65:
                code.append("BS208")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS090")
        if e>=70 and pm>=70 and p>=70:
            if avm>=85:
                code.append("SE922")
        if e>=65 and pm>=65 and ((c>=65 and p>=65) or (p>=65 and b>=65) or (b>=65 and c>=65)):
            if avm>=75:
                code.append("SQ150")
        if e>=55 and pm>=60:
            if avm>=65:
                code.append("BS020")
        if e>=50 and pm>=50 and (c>=50 and p>=50 and (b>=50 or hs>=50)):
            if avm>=60:
                code.append("U0105")
        if e>=65 and pm>=50 and (b>=50 and (c>=50 or p>=50)):
            if avm>=60:
                code.append("U0909")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i])  
            h_n_a_final.append(h_n_a_both[i])  

        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final

    ##############################################################################  Religion and Philosophy  #######################

    if major_program=="religion_and_philosophy":
        code=[]
        p_n_final=[]
        h_n_final=[]
        h_n_a=["كلية العلوم الشرعية","كلية العلوم الشرعية"]
        p_n_a=["الدين والفلسفة",'الدين والفلسفة']
        h_n_a_final=[]  
        p_n_a_final=[] 
        if gender=="male":
            gen="M"
        else:
            gen="F"
        if ar>=75 and islamic>=75 and avm>=75:
            if gen=="M":
                code.append("IS003")
            else:
                code.append("IS004")
        if len(code)!=0:
            if code[0]=="IS003":
                p_n_final.append("Jurisprudence And Its Foundations, Foundations of Religion")
                h_n_final.append("College of Sharia Sciences") 
                p_n_a_final.append(p_n_a[0])   
                h_n_a_final.append(h_n_a[0])

            elif code[0]=="IS004":
                p_n_final.append("Jurisprudence And Its Foundations, Foundations of Religion")
                h_n_final.append("College of Sharia Sciences")
                p_n_a_final.append(p_n_a[0])   
                h_n_a_final.append(h_n_a[0])
        code_final=code
        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final

    ################################################################################# Society and Culture ##########################################################

    if major_program=="society_and_culture":
        p_c_both=['BS077', 'BS219', 'BS221', 'BS197', 'BS198', 'BS072', 'BS075', 'BS231', 'BS033', 'BS036', 'BS188', 'BS092', 'BS093', 'SE925', 'SE926', 'SQ255', 'SQ700', 'SQ800', 'BS021', 'BS023', 'BS011']
        p_n_both=['Law', 'Law', 'Counselling Psychology', 'English Literature -English Professional Writing', 'Human Development and Family Studies', 'Business Economics', 'Translation', 'Law', 'Law', 'English Studies -English Language and Translation', 'English Language', 'Commercial Law', 'Economics', 'Arts', 'Social sciences', "College of Economics and Political Science's ( Political Science's)", 'College of Arts and Social Sciences (General Arts)', 'College of Law', 'Law', 'English Language and Literature -English Language and Translation', 'French Language and Translation -English Language and Translation -German Language and Translation']
        h_n_both=['Arab Open University', 'Al Sharqiyah University', 'Al Sharqiyah University', 'Bayan College', 'Bayan College', 'Al- Buraimi College', 'Al- Buraimi College', 'Buraimi University ', 'Dhofar University', 'Dhofar University', 'Majan College', 'Modern College of Business and Science', 'Modern College of Business and Science', 'External  Scholarships Department', 'External  Scholarships Department', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sohar  University', 'Sohar  University', 'University  of Nizwa']


        p_n_a_both=['القانون', 'القانون', 'الإرشاد النفسي ', 'الأدب الانجليزي -كتابة اللغة الإنجليزية الإحترافية', 'التنمية البشرية والدراسات الاسرية (دراسة الفرد والاسرة)', 'اقتصاد الاعمال', 'الترجمة', 'القانون', 'الحقوق', 'الترجمة - اللغة الإنجليزية', 'اللغة الإنجليزية', 'القانون التجاري', 'الاقتصاد', 'آداب', 'العلوم الإجتماعية', 'كلية الإقتصاد والعلوم السياسية (العلوم السياسية)', 'كلية الآداب والعلوم الإجتماعية (آداب عام)', 'كلية الحقوق ', 'القانون', 'اللغة الانجليزية وأدابها -اللغة الإنجليزية والترجمة', 'اللغة الفرنسية والترجمة -اللغة الالمانية والترجمة -اللغة الإنجليزية والترجمة']


        h_n_a_both=[' الجامعة العربية المفتوحة', 'جامعة الشرقية', 'جامعة الشرقية', 'كلية البيان', 'كلية البيان', 'كلية البريمي', 'كلية البريمي', 'جامعة البريمي ', 'جامعة ظفار', 'جامعة ظفار', 'كلية مجان', 'الكلية الحديثة للتجارة والعلوم', 'الكلية الحديثة للتجارة والعلوم', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'جامعة السلطان قابوس', 'جامعة السلطان قابوس', 'جامعة السلطان قابوس', 'جامعة صحار', 'جامعة صحار', 'جامعة نزوى']

        p_n_a_final=[] 
        h_n_a_final=[] 

        if gender=="male":
            gen="M"
        else:
            gen="F"

        code=[]
        if e>=55 and ar>=75:
            if avm>=65:
                code.append("BS077")
                code.append("BS219")
        if e>=55 and ar>=60 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS221")
        if e>=80 and ar>=60:
            if avm>=65:
                code.append("BS197")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS198")
                code.append("BS072")
                code.append("BS075")
        if e>=55 and ar>=75:
            if avm>=65:
                code.append("BS231")
                code.append("BS033")
        if e>=80 and ar>=60:
            if avm>=65:
                code.append("BS036")
                code.append("BS188")
        if e>=55 and ar>=75:
            if avm>=65:
                code.append("BS092")
        if e>=55 and (am>=60 or pm>=60):
            if avm>=65:
                code.append("BS093")
        if e>=70 and ar>=70 and (am>=70 or pm>=70):
            if avm>=80:
                code.append("SE925")
        if e>=70 and ar>=70:
            if avm>=80:
                code.append("SE926")
        if e>=80 and ar>=80 and (am>=65 or pm>=65):
            if avm>=75:
                code.append("SQ255")
        if e>=65 and ar>=65 and islamic>=65:
            if avm>=75:
                code.append("SQ700")
                code.append("SQ800")
        if e>=55 and ar>=75:
            if avm>=65:
                code.append("BS021")
        if e>=80 and ar>=60:
            if avm>=65:
                code.append("BS023")
        if e>=65 and ar>=60:
            if avm>=65:
                code.append("BS011")
        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:
            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i])  
            h_n_a_final.append(h_n_a_both[i])  
        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final


    ###################################################################################### Education ###########################################################
    if major_program=="education":
        p_c_both=['BS222', 'BS223', 'BS240', 'BS241', 'BS242', 'BS009', 'BS039', 'BS040', 'PD010', 'PD011', 'ED006', 'ED007', 'ED008', 'ED009', 'ED010', 'SE924', 'SE930', 'SQ300', 'SQ350', 'SQ400', 'SQ410', 'SQ420', 'SQ500', 'SQ550', 'SQ600', 'SQ650', 'SQ660', 'SQ670', 'BS030', 'BS244', 'BS270', 'BS271', 'BS272', 'BS273', 'BS274', 'BS322', 'BS325', 'BS326', 'BS029', 'BS038', 'BS278', 'BS279', 'BS280', 'BS281', 'BS282', 'BS285', 'U1011', 'U1012', 'U1013', 'U1014', 'U1015', 'U1016', 'U1017', 'U1018', 'U1019']
        p_n_both=['Bachelor of Education (First Field )', 'Bachelor in Education (Second Field )', 'Bachelor of Education (Mathematics)', 'Bachelor of Education (Arabic Language)', 'Bachelor in Education (English Language)', 'Bachelor in Education (Computer)', ' Bachelor in Education (Mathematics)', 'Bachelor in Education (English Language)', 'First Field Teacher ', 'Second Field Teacher ', 'Mathematics for Secondary School Teaching', ' Physics for Secondary School Teaching', 'Chemistry for Secondary School Teaching', 'Biology for Secondary School Teaching', 'English for Secondary School Teaching', 'Education', 'College of Basic Education', 'College of Education (Science and Mathematics)', 'College of Education (Islamic Education)', 'التربية الإبتدائية (مجال أول)', 'التربية الإبتدائية (مجال ثاني)', 'Primary English Language', 'College of Education (English)', 'College of Education (Arabic)', 'College of Education (Physical Education)', 'College of Education (Art)', 'College of Education (Instructional & Teaching Technologies)', 'College of Education (Early Childhood)', 'Bachelor in Education (English Language)', 'Bachelor of Education (First Field)', 'Bachelor in Education (Mathematics)', 'Bachelor in Education (Arabic Language)', 'Bachelor in Education (Biology)', 'Bachelor in Education (physical education)', 'Bachelor in Education (Music)', 'Bachelor in Education (Arabic Language)', 'Bachelor in Education (physical education)', 'Bachelor in Education (Music)', 'Bachelor in Education (English Language)', 'Bachelor in Education (Mathematics)', 'Bachelor in Education (Arabic Language)', 'Bachelor in Education (Chemistry)', 'Bachelor in Education (Physics)', 'Bachelor in Education (Computer)', 'Bachelor in Education (Fine Arts)', 'Bachelor of Education (Biology)', 'Bachelor of English Language (Rustaq)', 'Bachelor of Education Mathematics (Rustaq)', 'Bachelor of Education Biology (Rustaq)', 'Bachelor of Education Chemistry (Rustaq)', 'Bachelor of Education Physics - (Rustaq)', 'Bachelor of Education Mathematics - Rustaq', 'Bachelor of Education Biology (Rustaq)', 'Bachelor of Education Chemistry (Rustaq)', 'Bachelor of Education Physics (Rustaq)']
        h_n_both=['Al Sharqiyah University', 'Al Sharqiyah University', 'Al Sharqiyah University', 'Al Sharqiyah University', 'Al Sharqiyah University', 'Dhofar University', 'Dhofar University', 'Dhofar University', 'Private Universities and Colleges', 'Private Universities and Colleges', 'External  Scholarships Department', 'External  Scholarships Department', 'External  Scholarships Department', 'External  Scholarships Department', 'External  Scholarships Department', 'External  Scholarships Department', 'External  Scholarships Department', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University,(Data not mentioned)', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sultan Qaboos University', 'Sohar  University', 'Sohar  University,(Data not mentioned)', 'Sohar  University', 'Sohar  University', 'Sohar  University', 'Sohar  University', 'Sohar  University', 'Sohar  University', 'Sohar  University', 'Sohar  University', 'University  of Nizwa', 'University  of Nizwa', 'University  of Nizwa', 'University  of Nizwa', 'University  of Nizwa', 'University  of Nizwa', 'University  of Nizwa', 'University  of Nizwa', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences', 'University of Technology and Applied Sciences']
        
        
        p_n_a_both=['بكالوريوس التربية (مجال أول)', 'بكالوريوس التربية (مجال ثاني)', 'بكالوريوس التربية (الرياضيات)', 'بكالوريوس التربية (اللغة العربية)', 'بكالوريوس التربية (اللغة الانجليزيه)', 'بكالوريوس التربية (تقنية المعلومات)', 'بكالوريوس التربية (الرياضيات)', 'بكالوريوس التربية (اللغة الانجليزية)', 'معلم مجال أول (للإناث فقط)', 'معلم مجال ثاني (للإناث فقط)', 'الرياضيات لتدريس المرحلة الثانوية', 'الفيزياء لتدريس المرحلة الثانوية', 'الكيمياء لتدريس المرحلة الثانوية', 'علم الأحياء لتدريس المرحلة الثانوية', 'اللغة الإنجليزية للتدريس في المدارس الثانوية', 'تربية', 'كلية التربية الأساسية', 'علوم ورياضيات', 'التربية إسلامية', 'التربية الإبتدائية (مجال أول)', 'التربية الإبتدائية (مجال ثاني)', 'اللغة الإنجليزية الأساسية', 'اللغة الإنجليزية', 'اللغة العربية', 'التربية الرياضية', 'التربية الفنية', 'تكنولوجيا التعليم والتعلم', 'طفل ما قبل المدرسة', 'بكالوريوس التربية (اللغة الانجليزيه)', 'بكالوريوس التربية (مجال أول)', 'بكالوريوس التربية (الرياضيات)', 'بكالوريوس التربية (اللغة العربية)', 'بكالوريوس التربية (الأحياء)', 'بكالوريوس التربية  (التربية الرياضية)', 'بكالوريوس تربية (التربية الموسيقية)', 'بكالوريوس التربية - توطين (اللغة العربية) ', 'بكالوريوس التربية - توطين  (التربية الرياضية)', 'بكالوريوس تربية - توطين (التربية الموسيقية)', 'بكالوريوس التربية (اللغة الانجليزيه)', 'بكالوريوس التربية (الرياضيات)', 'بكالوريوس التربية (اللغة العربية)', 'بكالوريوس التربية (الكيمياء)', 'بكالوريوس التربية (الفيزياء)', 'بكالوريوس التربية (تقنية المعلومات)', 'بكالوريوس التربية (التربية الفنية)', 'بكالوريوس التربية (الاحياء)', 'بكالوريوس تربية اللغة الإنجليزية (الرستاق)', 'بكالوريوس تربية رياضيات (الرستاق)', 'بكالوريوس تربية أحياء (الرستاق)', 'بكالوريوس تربية كيمياء (الرستاق)', 'بكالوريوس التربية فيزياء - (الرستاق)', 'بكالوريوس تربية رياضيات - التوطين (الرستاق)', 'بكالوريوس تربية احياء - التوطين (الرستاق)', 'بكالوريوس تربية كيمياء - التوطين (الرستاق)', 'بكالوريوس تربية فيزياء - التوطين (الرستاق) ']

        h_n_a_both=['جامعة الشرقية', 'جامعة الشرقية', 'جامعة الشرقية', 'جامعة الشرقية', 'جامعة الشرقية', 'جامعة ظفار', 'جامعة ظفار', 'جامعة ظفار', 'الجامعات والكليات الخاصة ', 'الجامعات والكليات الخاصة ', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'دائرة البعثات الخارجية', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة السلطان قابوس ', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة صحار', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'جامعة نزوى', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ', 'جامعة التقنية والعلوم التطبيقية ']

        p_n_a_final=[]  
        h_n_a_final=[] 
        
        
        
        if gender=="male":
            gen="M"
        else:
            gen="F"

        code=[]
        code_m=[]
        code_f=[]
        if e>=50 and (am>=50 or pm>=50):
            if avm>=80:
                if gen=="F":
                    code_f.append("BS222")
        if e>=50 and pm>=70 and (c>=70 or p>=70 or b>=70):
            if avm>=80:
                if gen=="F":
                    code_f.append("BS223")
        if e>=65 and pm>=70:
            if avm>=80:
                code.append("BS240")
        if e>=50 and (am>=50 or pm>=50):
            if avm>=80 and gen=="M":
                code_m.append("BS241")
            if avm>=80 and gen=="F":
                code_f.append("PD010")
        if e>=70 and (am>=50 or pm>=50):
            if avm>=80:
                code.append("BS242")
        if e>=65 and (am>=70 or pm>=70):
            if avm>=80 and gen=="M":
                code_m.append("BS009")
        if e>=65 and pm>=70:
            if avm>=80:
                code.append("BS039")
        if e>=70 and (am>=50 or pm>=50):
            if avm>=80:
                code.append("BS040")
        if pm>=70 and (c>=70 or p>=70 or c>=70):
            if avm>=80:
                code.append("PD011")
        if e>=90 and pm>=85:
            if avm>=85:
                code.append("ED006")
        if e>=90 and pm>=80 and p>=85:
            if avm>=85:
                code.append("ED007")
        if e>=90 and pm>=75 and c>=85:
            if avm>=85:
                code.append("ED008")
                code.append("ED009")
        if (am>=70 or pm>=70):
            if avm>=80:
                code.append("SE924")
                code.append("SE930")
        if e>=65 and ((b>=65 and c>=65 and p>=65) or (c>=65 and p>=65 and pm>=65) or (p>=65 and pm>=65 and b>=65) or (pm>=65 and b>=65 and c>=65)):
            if avm>=75:
                code.append("SQ300")
            if avm>=75 and gen=="F":
                code_f.append("SQ410")
        if e>=65 and islamic>=65 and e>=65 and ar>=65:
            if avm>=75:
                code.append("SQ350")
                code.append("SQ550")
            if avm>=75 and gen=="F":
                code_f.append("SQ400")
        if e>=90:
            if avm>=75 and gen=="F":
                code_f.append("SQ420")
        if e>=90 and islamic>=65 and ar>=65:
            if avm>=75:
                code.append("SQ500")
        if e>=65 and pe>=65 and ar>=65:
            if avm>=75:
                code.append("SQ600")
        if e>=65 and fa>=65 and ar>=65:
            if avm>=75:
                code.append("SQ650")
        if e>=65 and (pm>=65 or am>=65) and ar>=65:
            if avm>=75:
                code.append("SQ660")
        if e>=65 and islamic>=65 and ar>=65:
            if avm>=75 and gen=="F":
                code_f.append("SQ670")
        if e>=70:
            if avm>=80:
                code.append("BS030")
        # if gen=="F":
            # code_f.append("BS244")
        if pm>=70:
            if avm>=80:
                code.append("BS270")
        if islamic>=70 and ar>=70:
            if avm>=80 and gen=="M":
                code_m.append("BS271")
        if (pm>=65 or am>=65) and b>=70 and (c>=65 or p>=65):
            if avm>=80 and gen=="M":
                code_m.append("BS272")
        if pe>=70:
            if avm>=80 and gen=="F":
                code_f.append("BS273")
                code_f.append("BS325")
        if music>=70:
            if avm>=80:
                code.append("BS274")
                code.append("BS326")
        if islamic>=70 and ar>=70:
            if avm>=80 and gen=="M":
                code_m.append("BS322")
        if e>=70:
            if avm>=80:
                code.append("BS029")
        if e>=65and pm>=70:
            if avm>=80:
                code.append("BS038")
        if islamic>=70 and ar>=70:
            if avm>=80 and gen=="M":
                code_m.append("BS278")
        if e>=65 and pm>=65 and c>=70 and (b>=65  or p>=65):
            if avm>=80 and gen=="M":
                code_m.append("BS279")
        if e>=65 and pm>=65 and p>=70 and (b>=65 or c>=65):
            if avm>=80:
                code.append("BS280")
        if e>=65 and (am>=70 or pm>=70):
            if avm>=80 and gen=="M":
                code_m.append("BS281")
        if fa>=70:
            if avm>=80:
                code_m.append("BS282")
        if (am>=65 or pm>=65) and b>=70 and (c>=65 or p>=65):
            if avm>=80 and gen=="M":
                code_m.append("BS285")
        if e>=75 and islamic>=50 and ar>=50:
            if avm>=50:
                code.append("U1011")
        if e>=50 and pm>=65:
            if avm>=50:
                code.append("U1012")
        if e>=50 and (am>=50 or pm>=50) and b>=65 and (c>=50 or p>=50):
            if avm>=50:
                code.append("U1013")
        if e>=50 and pm>=50 and c>=65 and (b>=50 or p>=50):
            if avm>=50:
                code.append("U1014")
        if e>=50 and pm>=50 and p>=65 and (b>=50 or c>=50):
            if avm>=50:
                code.append("U1015")
        if e>=50 and pm>=60:
            if avm>=50:
                code.append("U1016")
        if e>=50 and (pm>=50 and am>=50) and b>=60 and (c>=50 or p>=50):
            if avm>=50:
                code.append("U1017")
        if e>=50 and pm>=50 and c>=60 and (b>=50 or p>=50):
            if avm>=50:
                code.append("U1018")
        if e>=50 and pm>=50 and p>=60 and (b>=50 or c>=50):
            if avm>=50:
                code.append("U1019")      

        indexes=[]
        for i in code:
            indexes.append(p_c_both.index(i))
        code_final=code
        p_n_final=[]
        h_n_final=[]
        for i in indexes:

            p_n_final.append(p_n_both[i])
            h_n_final.append(h_n_both[i])
            p_n_a_final.append(p_n_a_both[i]) 
            h_n_a_final.append(h_n_a_both[i])


        if gen=="F":
            indexes=[]
            for i in code_f:
                indexes.append(p_c_both.index(i))
            code_final+=code_f
            for i in indexes:
                p_n_final.append(p_n_both[i])
                h_n_final.append(h_n_both[i])
                p_n_a_final.append(p_n_a_both[i]) 
                h_n_a_final.append(h_n_a_both[i])

        if gen=="M":
            indexes=[]
            for i in code_m:
                indexes.append(p_c_both.index(i))
            code_final+=code_m
            for i in indexes:
                p_n_final.append(p_n_both[i])
                h_n_final.append(h_n_both[i])
                p_n_a_final.append(p_n_a_both[i]) 
                h_n_a_final.append(h_n_a_both[i])



        final=[]
        final=[code_final,p_n_final,h_n_final,p_n_a_final,h_n_a_final]
        return final
