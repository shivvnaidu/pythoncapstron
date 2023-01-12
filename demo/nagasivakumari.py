import pytest
class Test_nagasivakumari:
    @pytest.mark.parametrize("n,r",[(10,[1,2,5,10]),(1,[1]),(2,[1,2]),(2,[1,2]),(15,[1,3,5,15])])
    def test_factors(self,n,r):
        l1=[]
        for i in range(1,n+1):
            if(n%i==0):
                l1.append(i)
        if r==l1:
            assert True
        else:
            assert False
            @pytest.mark.parametrize("s,l"[("group2",["group1","group2","group3"]),("hcl",["hcl","HCL"])])
            def test_StringExist(self,s,l):
                if s in l:
                    assert True
                else:
                    assert False
            @pytest.mark.parametrize("l,l1",[([4,2,1,3],[4,3,2,1])])
            def test_Sort(self,l,l1):
                l2=sorted(l)
                if l2[::-1]==l1:
                    assert True
                else:
                    assert False

            @pytest.mark.parametrize("l,l1"[([4,2,1,3],3),([4,3,2,1],3)])
            def test_secondlargest(self,l,r):
                l1=l(set(l))
                l2=sorted(l1)
                if l2[-2]==r:
                    assert True
                else:
                    assert False
