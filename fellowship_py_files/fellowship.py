from flask import Flask, render_template, send_file, Blueprint
from fellowship_py_files.fellowship_definitions import *


fellowship_blueprint = Blueprint('fellowship', __name__)


def fellowship_function(app):
    @fellowship_blueprint.route('/fellowship', methods=['GET', 'POST'])
    def fellowship():

        total_count = applications_today()
        visitor_counts = visitor_count()

        # Application Status wise candidate count
        accepted_count = accepted_year_count()
        rejected_count = rejected_year_count()
       
        #Year wise total count  
        yr_twenty_count = twenty_count()         # Year 2020
        yr_twentyOne_count = twentyOne_count()   # Year 2021
        yr_twentyTwo_count = twentyTwo_count()   # Year 2022
        current_count = current_year_count()     # Year 2023
        yr_twentyFour_count = twentyFour_count() # Year 2024

        #Gender wise total count  
        male_count = male_student_count()     
        female_count = female_student_count()  

        #Yearwise Male count
        yr_twenty_count_male = male_twenty_count()              # Year 2020
        yr_twentyOne_count_male = male_twentyOne_count()        # Year 2021
        yr_twentyTwo_count_male= male_twentyTwo_count()         # Year 2022
        yr_twentyThree_count_male = male_twentyThree_count()    # Year 2023
        yr_twentyFour_count_male = male_twentyFour_count()      # Year 2024

        #Yearwise Female count
        yr_twenty_count_female = female_twenty_count()          # Year 2020
        yr_twentyOne_count_female = female_twentyOne_count()    # Year 2021
        yr_twentyTwo_count_female = female_twentyTwo_count()    # Year 2022
        yr_twentyThree_count_female = female_twentyThree_count()# Year 2023
        yr_twentyFour_count_female = female_twentyFour_count()  # Year 2024

        return render_template('masterDash/projects/fellowship.html', total_count=total_count, visitor_counts=visitor_counts,
                               current_count=current_count, 
                            # Application Status wise candidate count
                               accepted_count=accepted_count, rejected_count=rejected_count, 
                            #Yearwise total count    
                               yr_twenty_count=yr_twenty_count, yr_twentyOne_count=yr_twentyOne_count, 
                               yr_twentyTwo_count =yr_twentyTwo_count, yr_twentyFour_count=yr_twentyFour_count,
                            #Genderwise total count    
                               male_count=male_count, female_count=female_count, 
                            #Yearwise Male count   
                               yr_twenty_count_male=yr_twenty_count_male, yr_twentyOne_count_male=yr_twentyOne_count_male, yr_twentyTwo_count_male=yr_twentyTwo_count_male,
                               yr_twentyThree_count_male=yr_twentyThree_count_male, yr_twentyFour_count_male=yr_twentyFour_count_male,
                            #Yearwise Female count
                                yr_twenty_count_female=yr_twenty_count_female, yr_twentyOne_count_female=yr_twentyOne_count_female, 
                                yr_twentyTwo_count_female=yr_twentyTwo_count_female, yr_twentyThree_count_female=yr_twentyThree_count_female,
                                yr_twentyFour_count_female=yr_twentyFour_count_female

                            )