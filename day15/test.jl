struct ArrayMap{T, N} <: AbstractDict{Unsigned, T}
	array::Array{T, 1}
	is_set::BitArray{1}
	ArrayMap{T, N}() where {T, N} = new(Array{T, 1}(undef, N), falses(N))
end

Base.haskey(m::ArrayMap, key) = m.is_set[key + 1]

function Base.iterate(m::ArrayMap, i=1)
	for i in i:size(m.is_set, 1)
		if m.is_set[i]
			return (Pair(i - 1, m.array[i]), i + 1)
		end
	end
	return nothing
end

@inbounds function Base.setindex!(m::ArrayMap{T}, value::T, key::Unsigned) where T
	key += 1
	m.is_set[key] = true
	m.array[key] = value
end

@inbounds function Base.get(m::ArrayMap{T}, key::Unsigned, default::T) where T
	key += 1
	if haskey(m, key - 1)
		return m.array[key]
	end
	return default
end

function Base.length(m::ArrayMap)
	return sum(Iterators.filter(isone, m.is_set))
end

# println(methods(ArrayMap{Int, 10}))
# m = ArrayMap{Int, 100000}()
# @code_native setindex!(m, 1, 100)
# println(m)

function part(a::Array{Unsigned}, n::Int)
	# m::Dict{Int, Int} = Dict()
	m::Dict{Int, Int} = Dict{Int, Int}()
	# m::ArrayMap{Int, n} = ArrayMap{Int, n}()
	# m = ArrayMap{Unsigned, n}()
	next_ = 0
	for i in 0:n - 2
		if i < size(a, 1)
			next_ = i - get(m, a[i + 1], i)
			m[a[i + 1]] = i
			continue
		end
		# println(next_)
		say::Unsigned = next_
		next_ = i - get(m, say, i)
		m[say] = i
	end
	return next_
end

a = Array{Unsigned}([2, 1, 10, 11, 0, 6])

@time println(part(a, Int(3e7)))
