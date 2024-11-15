"""This is EX06 which usese dictionary"""

__author__ = "730827794"


def invert(input_dict:dict[str,str])->dict[str,str]:
    output_dict: dict[str,str]={}
    for key in input_dict:  
        value = input_dict[key] 
        if value in output_dict:
            raise KeyError("error message of your choice here!")
        output_dict[value] = key
    return output_dict   
        

def favorite_color(color_dict:dict[str, str])->str:
    color_list: list[str]=[]
    most_popular_color:str
    if len(color_dict)==0:
        return ""
    
    for key in color_dict:
        color_list.append(color_dict[key])
            
    frequency_dict:dict[str,int] = {}
    for color in color_list:
        if color in frequency_dict:
            frequency_dict[color] += 1
        else:
            frequency_dict[color] = 1
    
    current_max:int=0
    for key in frequency_dict:
        if frequency_dict[key]>current_max:
            current_max=frequency_dict[key]
            most_popular_color=key

    return most_popular_color


def count(original_list:list[str])->dict[str,int]:
    count_dict:dict[str,int]={}
    for item in original_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict

def alphabetizer(word_list:list[str])->dict[str, list[str]]:
    result_dict:dict[str,list[str]]={}
    for word in word_list:
        first_letter = word[0].lower()
        
        if first_letter in result_dict:
            result_dict[first_letter].append(word)
        
        else:
            result_dict[first_letter] = [word]            
    
    return result_dict

def update_attendance(attendance_dict:dict[str, list[str]],day:str,student:str)->None:
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day]=[student]