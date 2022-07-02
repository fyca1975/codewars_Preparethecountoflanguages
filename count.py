
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
                print(dic.values()) 
            

    
    print (dic) 

if __name__ == "__main__":
    list1 = [
            {'firstName': 'Zfsniy', 'lastName': 'Pcsdxzw', 'country': 'Vq', 'continent': 'Hvuip', 'age': 9, 'language': 'PHP'},
            {'firstName': 'G', 'lastName': 'Khw', 'country': 'Xqd', 'continent': 'Dqdu', 'age': 87, 'language': 'Java'}, 
            {'firstName': 'Hkobpl', 'lastName': 'Kwkzpt', 'country': 'Lrrakoj', 'continent': 'Wsmeadog', 'age': 41, 'language': 'Java'}, 
            {'firstName': 'Bmderpoc', 'lastName': 'Mzvaqaen', 'country': 'Qkhqsjii', 'continent': 'Wpijpnewrs', 'age': 42, 'language': 'PHP'}, 
            {'firstName': 'Arf', 'lastName': 'Ccufk', 'country': 'Zuouk', 'continent': 'Dbdy', 'age': 82, 'language': 'C'}, 
            {'firstName': 'Rz', 'lastName': 'Sgskgy', 'country': 'Udly', 'continent': 'W', 'age': 4, 'language': 'Ruby'}, 
            {'firstName': 'Gnwvekmkd', 'lastName': 'Mulpzr', 'country': 'V', 'continent': 'F', 'age': 70, 'language': 'Ruby'},
            {'firstName': 'Rpgrrla', 'lastName': 'Sxsgimze', 'country': 'Pyzti', 'continent': 'Nbpxbo', 'age': 19, 'language': 'JavaScript'}, 
            {'firstName': 'Pus', 'lastName': 'Nroayyhvrb', 'country': 'Gtq', 'continent': 'Lwkhmkz', 'age': 3, 'language': 'Python'}, 
            {'firstName': 'Yyuzhczf', 'lastName': 'Dqbw', 'country': 'J', 'continent': 'Puyec', 'age': 18, 'language': 'C'}, 
            {'firstName': 'Eevyeamw', 'lastName': 'Gihrqdaaga', 'country': 'Suvkbzg', 'continent': 'Nto', 'age': 68, 'language': 'JavaScript'}, 
            {'firstName': 'Pqqmmtiki', 'lastName': 'Sa', 'country': 'D', 'continent': 'Ylkg', 'age': 41, 'language': 'JavaScript'}, 
            {'firstName': 'Bchauvo', 'lastName': 'Mdptedggb', 'country': 'Pmgqyll', 'continent': 'Dhiaefpffs', 'age': 11, 'language': 'JavaScript'},
            {'firstName': 'Yeiuojp', 'lastName': 'Qhsk', 'country': 'Ev', 'continent': 'Dm', 'age': 58, 'language': 'PHP'},
            {'firstName': 'Fhjrjnbo', 'lastName': 'C', 'country': 'Gaixgw', 'continent': 'Zvrzav', 'age': 42, 'language': 'C'}, 
            {'firstName': 'Mouq', 'lastName': 'Oqpkdw', 'country': 'Clkd', 'continent': 'Ejwxd', 'age': 86, 'language': 'Ruby'}, 
            {'firstName': 'Bywn', 'lastName': 'Vf', 'country': 'Epso', 'continent': 'Qw', 'age': 36, 'language': 'Clojure'}, 
            {'firstName': 'Ajwvs', 'lastName': 'Ytz', 'country': 'Suykd', 'continent': 'Gbsdv', 'age': 10, 'language': 'Python'}, 
            {'firstName': 'Mkg', 'lastName': 'Tb', 'country': 'Uep', 'continent': 'Fzisz', 'age': 20, 'language': 'Ruby'}, 
            {'firstName': 'N', 'lastName': 'Tywuqmqpp', 'country': 'Uhaxgnkc', 'continent': 'Zc', 'age': 49, 'language': 'JavaScript'}
            ]  
    count_languages(list1)
    real = {'PHP': 3, 'Java': 2, 'C': 4, 'Ruby': 4, 'JavaScript': 5, 'Python': 2, 'Clojure': 1} 
    print(real)
    # Resuñtado
    #{'PHP': 3, 'Java': 2, 'C': 4, 'Ruby': 4, 'JavaScript': 5, 'Python': 2, 'Clojure': 1} should equal {'PHP': 3, 'Java': 2, 'C': 3, 'Ruby': 4, 'JavaScript': 5, 'Python': 2, 'Clojure': 1}