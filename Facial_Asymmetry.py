def main(csvfile, SubjIDs):    
    ##############################################
    #  Checking if the file provided is readable #
    ##############################################
    try:
        check = 0
        f = open(csvfile, "r")
        f.close()

    except:
        check = 3

    ##############################################
    #   Checking if the value provided is valid  #
    ##############################################

    if (len(SubjIDs) != 2):
        check = 2 

    if(check == 2):
        print("The subjectIDs inputs is invalid. Please ensure that you entered only two correct SubjectIDs. Thank you")
        #return None
    
    ######################################
    #  Opening the file to read the data #
    ######################################

    with open(csvfile, 'r') as f:
        subjID1 = []
        subjID2 = []

        ######################################
        # For loop to extract data into List #
        ######################################
        for line in f:
            words = line.split(',')

            if(words[0] == SubjIDs[0]):
                subjID1.append(words) 

            elif(words[0] == SubjIDs[1]):
                subjID2.append(words)

    ########################################
    #  Checking if input's subjectID exist #
    ########################################

    if (len(subjID1) == 0 or len(subjID2) == 0):
        check = 2

    ########################################################
    #  Ensuring both datasets is not corrupted [require 7] #
    ########################################################

    if (len(subjID1) < 7 and len(subjID1) > 0):
        check = 1

    ###################################
    #  The 'csvfile' input is invalid #
    ###################################

    if(check == 3):
        print("Your file cannot be found or opened. Please ensure the file provided exist or spelled correctly. Thank you")
        return None, None, None, None

    ###################################
    #  The 'subjID' input is invalid  #
    ###################################

    elif(check == 2):
        print("The subjectIDs inputs doesn't exist. Please ensure that you entered the correct SubjectID. Thank you")
        exit

    ###########################################
    #  The dataset corrupted (Missing value)  #
    ###########################################

    elif(check == 1):
        return None, None, None, None

    #######################################
    #  All the input values are validated #
    #######################################

    else:
        
        #######
        # OP1 #
        #######

        ######################
        # Adjusting the list #
        ######################
        
        for i in range(1,8):
            subjID1[i-1][7] = str(subjID1[i-1][7]).replace("\n","")
            subjID2[i-1][7] = str(subjID2[i-1][7]).replace("\n","")

        ###########################
        #  Checking Nose Tip == 0 #
        ###########################
        prn_check = 0

        #######################################
        #  Nose tip Check (SubjID1 & SubjID2) #
        #######################################

        prn_val = [((float(subjID1[i-1][5]) - float(subjID1[i-1][2]))**2 + ((float(subjID1[i-1][6]) - float(subjID1[i-1][3]) )**2) + (float(subjID1[i-1][7]) - float(subjID1[i-1][4]))**2 )**0.5 , ((float(subjID2[i-1][5]) - float(subjID2[i-1][2]))**2 + ((float(subjID2[i-1][6]) - float(subjID2[i-1][3]) )**2) + (float(subjID2[i-1][7]) - float(subjID2[i-1][4]))**2 )**0.5]
        
        for i in range(2):
            if(prn_val[i] != 0.0):
                prn_check = 1

        if(prn_check == 0):
            #####################################
            #  initialized the values into DICT #
            #####################################

            asyID1 = {}
            asyID2 = {}

            #####################################################
            #  For loop to calculate the 3D asymmetry (SubjID1) #
            #####################################################

            for i in range(1,7):
                asyID1[str(subjID1[i-1][1]).upper()] = round(((float(subjID1[i-1][5]) - float(subjID1[i-1][2]))**2 + ((float(subjID1[i-1][6]) - float(subjID1[i-1][3]) )**2) + (float(subjID1[i-1][7]) - float(subjID1[i-1][4]))**2 )**0.5 ,4)

            #####################################################
            #  For loop to calculate the 3D asymmetry (SubjID2) #
            #####################################################

            for i in range(1,7):
                asyID2[str(subjID2[i-1][1]).upper()] = round(((float(subjID2[i-1][5]) - float(subjID2[i-1][2]))**2 + ((float(subjID2[i-1][6]) - float(subjID2[i-1][3]) )**2) + (float(subjID2[i-1][7]) - float(subjID2[i-1][4]))**2 )**0.5 ,4)

            ##########################
            #  Returning OP1 results #
            ##########################

            op1_list = [asyID1, asyID2]

        else:
            op1_list = None

        #######
        # OP2 #
        #######

        #####################################
        #  initialized the values into DICT #
        #####################################

        eucID1 = {}
        eucID2 = {}
        counter = 0
        i = 1

        ################################################################
        #  While loop to calculate the 3D Euclidean Distance (SubjID1) #
        ################################################################

        while(True):

            if(counter == 6):
                i = 1
                counter = 0
                break

            else:

                if(i == 3):
                    eucID1[str(subjID1[i][1]).upper() + str(subjID1[i-2][1]).upper()] = round(((float(subjID1[i][2]) - float(subjID1[i-2][2]))**2 + ((float(subjID1[i][3]) - float(subjID1[i-2][3]) )**2) + (float(subjID1[i][4]) - float(subjID1[i-2][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

                elif(i == 4):
                    eucID1[str(subjID1[i-4][1]).upper() + str(subjID1[i][1]).upper()] = round(((float(subjID1[i][2]) - float(subjID1[i-4][2]))**2 + ((float(subjID1[i][3]) - float(subjID1[i-4][3]) )**2) + (float(subjID1[i][4]) - float(subjID1[i-4][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

                elif(i == 5):
                    eucID1[str(subjID1[i-1][1]).upper() + str(subjID1[i][1]).upper()] = round(((float(subjID1[i][2]) - float(subjID1[i-1][2]))**2 + ((float(subjID1[i][3]) - float(subjID1[i-1][3]) )**2) + (float(subjID1[i][4]) - float(subjID1[i-1][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

                elif(i == 6):
                    eucID1[str(subjID1[i-1][1]).upper() + str(subjID1[i-6][1]).upper()] = round(((float(subjID1[i-6][2]) - float(subjID1[i-1][2]))**2 + ((float(subjID1[i-6][3]) - float(subjID1[i-1][3]) )**2) + (float(subjID1[i-6][4]) - float(subjID1[i-1][4]))**2 )**0.5 ,4)
                    counter +=1   

                else:         
                    eucID1[str(subjID1[i][1]).upper() + str(subjID1[i+1][1]).upper()] = round(((float(subjID1[i+1][2]) - float(subjID1[i][2]))**2 + ((float(subjID1[i+1][3]) - float(subjID1[i][3]) )**2) + (float(subjID1[i+1][4]) - float(subjID1[i][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

        ################################################################
        #  While loop to calculate the 3D Euclidean Distance (SubjID2) #
        ################################################################

        while(True):

            if(counter == 6):
                break

            else:

                if(i == 3):
                    eucID2[str(subjID2[i][1]).upper() + str(subjID2[i-2][1]).upper()] = round(((float(subjID2[i][2]) - float(subjID2[i-2][2]))**2 + ((float(subjID2[i][3]) - float(subjID2[i-2][3]) )**2) + (float(subjID2[i][4]) - float(subjID2[i-2][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

                elif(i == 4):
                    eucID2[str(subjID2[i-4][1]).upper() + str(subjID2[i][1]).upper()] = round(((float(subjID2[i][2]) - float(subjID2[i-4][2]))**2 + ((float(subjID2[i][3]) - float(subjID2[i-4][3]) )**2) + (float(subjID2[i][4]) - float(subjID2[i-4][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

                elif(i == 5):
                    eucID2[str(subjID2[i-1][1]).upper() + str(subjID2[i][1]).upper()] = round(((float(subjID2[i][2]) - float(subjID2[i-1][2]))**2 + ((float(subjID2[i][3]) - float(subjID2[i-1][3]) )**2) + (float(subjID2[i][4]) - float(subjID2[i-1][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

                elif(i == 6):
                    eucID2[str(subjID2[i-1][1]).upper() + str(subjID2[i-6][1]).upper()] = round(((float(subjID2[i-6][2]) - float(subjID2[i-1][2]))**2 + ((float(subjID2[i-6][3]) - float(subjID2[i-1][3]) )**2) + (float(subjID2[i-6][4]) - float(subjID2[i-1][4]))**2 )**0.5 ,4)
                    counter +=1   

                else:         
                    eucID2[str(subjID2[i][1]).upper() + str(subjID2[i+1][1]).upper()] = round(((float(subjID2[i+1][2]) - float(subjID2[i][2]))**2 + ((float(subjID2[i+1][3]) - float(subjID2[i][3]) )**2) + (float(subjID2[i+1][4]) - float(subjID2[i][4]))**2 )**0.5 ,4)
                    i += 1
                    counter +=1

        ##########################
        #  Returning OP2 results #
        ##########################

        op2_list = [eucID1, eucID2]

        #######
        # OP3 #
        #######

        ###########################
        #  Initializing OP3 Value #
        ###########################

        op3_list = []

        ######################################
        #  Opening the file to read the data #
        ######################################

        with open(csvfile, 'r') as f:
            subjID3 = []
            total_val = {}

            ######################################
            # For loop to extract data into List #
            ######################################
            for line in f:
                words = line.split(',')
                subjID3.append(words) 

            ######################
            # Adjusting the list #
            ######################
            
            for i in range(1,len(subjID3)):
                subjID3[i-1][7] = str(subjID3[i-1][7]).replace("\n","")

        #######################################################
        #  Ensuring the datasets is not corrupted [require 7] #
        #######################################################

        if (len(subjID3) % 7 == 0):
            
            ###################################################
            #  Calculating the 3D Asymmetries for each subjID #
            ###################################################

            for i in range(1,len(subjID3)):
                if (subjID3[i][0] in total_val):
                    total_val[str(subjID3[i][0]).upper()] += ((float(subjID3[i][5]) - float(subjID3[i][2]))**2 + ((float(subjID3[i][6]) - float(subjID3[i][3]) )**2) + (float(subjID3[i][7]) - float(subjID3[i][4]))**2 )**0.5
                else:
                    total_val[str(subjID3[i][0]).upper()] = ((float(subjID3[i][5]) - float(subjID3[i][2]))**2 + ((float(subjID3[i][6]) - float(subjID3[i][3]) )**2) + (float(subjID3[i][7]) - float(subjID3[i][4]))**2 )**0.5

            ################################
            #  Rounding to 4 Decimal place #
            ################################

            for k, v in total_val.items():
                total_val[k] = round(v,4)

            ###############################################
            #  Converting Dict to tuple and getting Top 5 #
            ###############################################

            op3_list = [(k, v) for k, v in total_val.items()]
            op3_list = sorted(op3_list, key=lambda tup:(tup[1]))[:5]

        else:
            op3_list = None

        #######
        # OP4 #
        #######

        #######################################
        #  Initialize Cosine Similarity Score #
        #######################################

        op4_val = 0.0

        ########################################
        #  Calculating Cosine Similarity Score #
        ########################################

        op4_val = round(((op2_list[0]["EXEN"] * op2_list[1]["EXEN"]) + (op2_list[0]["ENAL"] * op2_list[1]["ENAL"] ) + (op2_list[0]["ALEX"] * op2_list[1]["ALEX"]) + (op2_list[0]["FTSBAL"] * op2_list[1]["FTSBAL"]) + (op2_list[0]["SBALCH"] * op2_list[1]["SBALCH"]) + (op2_list[0]["CHFT"] * op2_list[1]["CHFT"])) \
            / (((op2_list[0]["EXEN"]**2 + op2_list[0]["ENAL"]**2 + op2_list[0]["ALEX"]**2 + op2_list[0]["FTSBAL"]**2 + op2_list[0]["SBALCH"]**2 + op2_list[0]["CHFT"]**2)**0.5) * ((op2_list[1]["EXEN"]**2 + op2_list[1]["ENAL"]**2 + op2_list[1]["ALEX"]**2 + op2_list[1]["FTSBAL"]**2 + op2_list[1]["SBALCH"]**2 + op2_list[1]["CHFT"]**2)**0.5)),4)

        #################################
        #  Returning All Output results #
        #################################

        return op1_list, op2_list, op3_list, op4_val

#if __name__ == '__main__': 
    #OP1, OP2, OP3, OP4 = main('SampleData.csv', ["B7033", "C1283"])
