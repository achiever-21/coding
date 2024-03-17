class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        count=0
        if n1>n2:
            head1,head2=head2,head1 
        set1=set()
        while head1:
            set1.add(head1.data)
            head1=head1.next
        node2=head2 
        while node2:
            a=node2.data 
            if a>x:
                pass
            elif x-a in set1:
                count+=1 
            node2=node2.next 
        return count
            
