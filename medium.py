


import requests, time, pandas, random, json, os
import numpy as np
from dotenv import load_dotenv

load_dotenv()

def Medium(inputNumber, PandasDataFrame, **kwargs): # this is the function, it's name, two required inputs and **kwargs for variable input

    print(f'secret key: {os.getenv("SECRET_KEY")} \n')

    #let's keep track of our function :)
    start_time = time.time()

    #retrieving fact of the day
    request = requests.get('https://catfact.ninja/fact')
    response = json.loads(request.content)['fact']
    print(f'cat fact of the day:\n{response}\n')

    # dictionairy used to store the ouput of this function
    # this will be returned - on error, or when completed
    dict_output = {
        'errors' : {}
    }
    
    #overkill here, but we showcase some checks, exception and adding this to the dictionairy
    try:
        inputNumber = int(inputNumber)
    except Exception as e:
        dict_output['errors'] = f'couldn\'t convert the input number \n {e}'

    #We do some maths (modulo -> check it out), use the _ as holder for a variable
    if inputNumber % 5 == 0:
        _ = inputNumber ** inputNumber + 2
        dict_output['out'] = f'the first pass {_}'
        

    #let's check out the kwargs
    if kwargs:
        print(f'these are the provided **kwargs -- Uhumm I already knew chips are nice!\n{kwargs}\n')

    # ok let's do some stuff with the data from the Pandas DataFrame https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    if PandasDataFrame.empty:
        return dict_output

    #numbers is a column named in the Pandas DataFrame containing a random series of nmbers
    list_of_numbers = PandasDataFrame['numbers'].to_list()
    list_of_adjusted_numbers = [n + 5 * 3 for n in list_of_numbers if lambda n : n > 35 * 2]
    dict_output['password'] = '.'.join([str(x) for x in [np.median(list_of_adjusted_numbers), 1, 0, 1, 1]])

    #calculate the end
    print(f'it took us roughly {time.time() - start_time} seconds to complete this, thanks PC\n')

    return json.dumps(dict_output, indent=1)

    if dict_output:
         
        #elipsis -> can be used to fill parts you will develop later, or not at all 
        #-> i find it convenient to use it here to avoid open space

        ...

frame = pandas.DataFrame(columns=['numbers'])
frame['numbers'] = np.linspace(random.randint(1, 5), random.randint(35, 125), dtype=int)
print(f'{frame.describe}\n')

print(Medium(35, frame, friet='lekker')) # -> providing a number (35), a pandas.DataFrame and the **kwargs named 'friet' which is lekker (nice)
    
         
    
        



