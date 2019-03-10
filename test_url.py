ul = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.785d7b19nELJh6&s={}&q=iiphone+x&sort=s&style=g&from=.list.pc_1_searchbutton&smAreaId=110100&type=pc#J_Filter'
for i in range(120, 900, 60):
    url = ul.format(i)
    print(url)