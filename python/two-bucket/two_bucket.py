def measure(bucket_one, bucket_two, goal, start_bucket):
    if start_bucket is 'two':
    	#swap buckets
    	bucket_one += bucket_two
    	bucket_two = bucket_one - bucket_two
    	bucket_one = bucket_one - bucket_two
    	b1_name = 'two'
    	b2_name = 'one'
    else:
    	b1_name = 'one'
    	b2_name = 'two'
    
    max_bucket_one = bucket_one
    max_bucket_two = bucket_two

    bucket_two = 0
    steps_count = 1

    if(max_bucket_two == goal):
    	return (steps_count + 1, b2_name, bucket_one)
    while True:
    	if bucket_one == goal:
    		return (steps_count, b1_name, bucket_two)
    		
    	elif bucket_two == goal:
    		return (steps_count, b2_name, bucket_one)

    	elif bucket_one is 0:
    		bucket_one = max_bucket_one;
    		steps_count += 1
    		continue

    	elif bucket_two is max_bucket_two:
    		bucket_two = 0
    		steps_count += 1
    		continue

    	elif bucket_two < max_bucket_two:
    		water_shift = min(bucket_one, max_bucket_two - bucket_two)
    		bucket_two += water_shift
    		bucket_one -= water_shift
    		steps_count += 1
    		continue