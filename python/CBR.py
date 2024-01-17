def tech(set):
    set.add(56)
    print("inside",set) //{43,22,34,56}
set1={43,22,34}
tech(set1)
print("outside",set1)   //{43,22,34,56} it will update both inside fun & outside fun