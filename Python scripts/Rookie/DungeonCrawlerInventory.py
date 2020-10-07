import pprint

def displayInventory (inventory):
    count=0
    def isPlural(qty):
        if qty>1:
            return 's'
        return ''
            
    for item in inventory:
        count+=inventory[item]
        print(str(inventory[item])+' '+item+isPlural(inventory[item]))
    print('Total number of items :'+str(count))

def addToInventory(inventory,loot):
    
    for i in range(len(loot)):
        found=0
        for item in inventory.keys():
            if loot[i] == item:
                found=1
                inventory[item]+=1
        if found == 0:
            inventory[loot[i]]=1
    

inventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inventory,dragonLoot)

displayInventory(inventory)
