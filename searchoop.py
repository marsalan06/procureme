from googlesearch import search

class Search_google:
    def __init__(self,part,descript,hits=5,site_ref=None,region="Pakistan"): 
        """ part==> from Watson, descript==> mech,elec,etc, hits==> no of sites, site_ref==> any other domain"""
        """ regin==> in pakistan or others"""
        self.part=part
        self.descript=descript
        self.hits=hits
        self.site_ref=site_ref 
        self.region=region

    def perform_search(self):
        res=[]
        if self.site_ref== None:
            l=["BuyAliexpress", "BuyAliBaba", "Buydaraz"]
        else:
            y="Buy"+str(self.site_ref)
            l=["BuyAliexpress", "BuyAliBaba", "Buydaraz"] 
            l.insert(0,y)
            #print(l)

        for i in l:
            query = str(self.descript)+ str(self.part)+str(self.region) + i
            for j in search(query, tld="com", num=int(self.hits), stop=int(self.hits), pause=2): 
                res.append(j)
        return(res)

if __name__=="__main__":
    result=Search_google("Spring","Mechanical",hits=2,site_ref="facebook")
    resl=result.perform_search()
    for i in resl:
        print(i)