def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    print("BMI = " + str(bmi))
    
    # Determine weight classification
    if bmi < 18.5:
        print("Classification: Under Weight")
    elif 18.5 <= bmi <= 25.0:
        print("Classification: Normal Weight")
    else:
        print("Classification: Over Weight")

# Call the function with height and weight
calculate_bmi(weight=57, height=1.73)
