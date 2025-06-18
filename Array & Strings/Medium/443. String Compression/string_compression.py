class Solution:
    def compress(self, chars: List[str]) -> int:
        i,idx,n = 0, 0, len(chars)

        # Process the entire character list
        while i < n:
            # Move i pointer to end of current character sequence
            count=1
            while (count+i) < n and chars[count+i] == chars[i]:
                count += 1

            # Write the current character to the idx pointer
            chars[idx] = chars[i]
            idx += 1

            # If we have a sequence longer than 1
            if count > 1:
                # Convert count to string and write each digit
                string = str(count)
                chars[idx:idx+len(string)]=list(string)
                idx+=len(string)
            i+=count

        # Return the length of the compressed list
        return idx
