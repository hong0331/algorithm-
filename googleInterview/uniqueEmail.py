class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
      
        list=[]
        for localname in emails: 
            # case1 : '.' in the localname can exist in multiple times 
            # case 2: '.' in the domain should be preserved 
            while '.' in localname and localname.index('.') < localname.index('@'):  
                localname=localname[:localname.index('.')]+localname[localname.index('.')+1:]
                
            # case 3: the string after '+' in the localname should be deleted.
            if '+' in localname and localname.index('+') < localname.index('@'):
                 localname=localname[:localname.index('+')]+localname[localname.index('@'):]
            
            list.append(localname)    
            
    
        print(list)
        results=set(list)
        return (len(results))
        

    '''
       localname=localname.replace('.','') => problem 1: remove '.' in the domain name 


       Comment: Took 40 min, need to think more about the cases before writing the code 
    '''
       
            
