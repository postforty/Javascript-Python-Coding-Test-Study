 temp_list[-1] == j[idx]:
                    temp_list.pop()
                    answer += 2
                else:
                    temp_list.append(j[idx])
                j[idx] = 0
                break