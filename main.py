
l1=["Ivana","Marko","Lovro","Ana","Ena"]

print("broj elementa u l1 je: ",len(l1))

if "Ana" in l1:
  print("je li ana u l1:", "da")
else:
  print("ne")

l1.sort(reverse=True)
print(l1)
print("prvo slovo zadnjeg imena je:",l1[4][0])
