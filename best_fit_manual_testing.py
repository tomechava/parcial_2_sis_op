
def best_fit(work_memory, req, index):
    best_pos = -1

    for j in range(len(work_memory)):  #Cicle between memory blocs
        block_addr, block_size = work_memory[j]
        
        if block_size == req:  #If exactly same size
            best_pos = j
            break
        elif block_size > req:   #Process size fits in the blocks size?
                if best_pos == -1 or work_memory[j][1] < work_memory[best_pos][1]: #Block size smaller than past size or first available position
                    best_pos = j
    
    if best_pos != -1:  #If best allocation found...
        best_block_addr, best_block_size = work_memory[best_pos]
        new_addr = best_block_addr + req 
        new_size = best_block_size - req
        
        work_memory[best_pos] = (new_addr, new_size)

        if new_size == 0:       #If memory block full, delete
            del work_memory[best_pos]
            
        return [work_memory, new_addr, new_size, best_pos]
    
    
    return None
            
            
        
if __name__ == '__main__':
    work_memory = [(0x100, 0x104), 
                   (0x200, 0x150), 
                   (0x350, 0x1F0), 
                   (0x540, 0xC8), 
                   (0x608, 0x1C2), 
                   (0x800, 0xD2)]
    
    req = 0x1C4

    index = 0
    
    print(best_fit(work_memory, req, index))