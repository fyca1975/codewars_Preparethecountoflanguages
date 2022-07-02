
def count_languages(lst): 
    # your code here
    dic = {}
    for elem in lst:      
        for k,v in elem.items():
            if k == 'language':
                dic.setdefault(v ,0)
                print(k, v)
            if v in dic:
                dic[v] += 1 
                print(dic.values(), dic.keys() ) 
            

    
    print (dic) 

if __name__ == "__main__":
    list1 = [
            { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
            { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
            { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
            { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
            ]  
    count_languages(list1)

    # la respuesta que debe retornar es {'C': 2, 'JavaScript': 1, 'Ruby': 1}