from multiprocessing import Pool

def heavy_task(n):
    return sum(i * i for i in range(n))

if __name__ == "__main__":
    with Pool(4) as pool:
        results = pool.map(heavy_task, [1000000] * 4)

    print(results)
