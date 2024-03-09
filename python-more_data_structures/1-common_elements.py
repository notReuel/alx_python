def common_elements(set_1, set_2):
    c_set = {x for x in set_1 if x in set_2}
    return c_set
    

set_1 = { "Python", "C", "Javascript" }
set_2 = { "Bash", "C", "Ruby", "Perl" }
if __name__=="__main__":
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))