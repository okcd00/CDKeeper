class Solution {
public :
	int majorityElement( vector< int > & num ) 
	{
		int count = 1;
		int target = num[0];

		for( int i = 1; i < num.size(); ++i )
		{
			// if( !count ) { target = num[i]; count = 1; continue; }
			if( !count ) target = num[i];          
			if( target == num[i] ) ++count;
			else --count;
		}
		return target;
	}
};