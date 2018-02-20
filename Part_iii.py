from scipy.stats import norm


def find_gaussian(x, mean, std_dev):
    return norm.pdf(x, mean, std_dev)


def give_likelihood(rx, ry, bx, by, std_dev):
    likelihood_dict = {}
    prx1 = find_gaussian(rx, 0, std_dev)
    pry1 = find_gaussian(ry, 1, std_dev)
    pbx1 = find_gaussian(bx, 0, std_dev)
    pby1 = find_gaussian(by, 1, std_dev)
    likelihood_dict['up'] = prx1*pry1*pbx1*pby1
    pry2 = find_gaussian(ry, -1, std_dev)
    pby2 = find_gaussian(by, -1, std_dev)
    likelihood_dict['down'] = prx1*pry2*pbx1*pby2
    prx3 = find_gaussian(rx, -1, std_dev)
    pry3 = find_gaussian(ry, 0, std_dev)
    pbx3 = find_gaussian(bx, -1, std_dev)
    pby3 = find_gaussian(by, 0, std_dev)
    likelihood_dict['left'] = prx3*pry3*pbx3*pby3
    prx4 = find_gaussian(rx, 1, std_dev)
    pbx4 = find_gaussian(bx, 1, std_dev)
    likelihood_dict['right'] = prx4*pry3*pbx4*pby3
    return likelihood_dict


if __name__ == "__main__":
    # Task 1
    prior = 0.25
    rxx = 0.75
    ryy = -0.6
    bxx = 1.4
    byy = -0.2
    stan_dev = 1
    likelihood = give_likelihood(rxx, ryy, bxx, byy, stan_dev)
    posterior = {}
    for k in likelihood:
        posterior[k] = likelihood[k]*prior

    sum_post = sum(posterior.values())
    posterior = {k: v / sum_post for k, v in posterior.items()}
    direction = max(posterior, key=lambda key: posterior[key])
    print('inferred direction of motion is : {}'.format(direction))

    # Task 2
    stan_dev = 5
    likelihood = give_likelihood(rxx, ryy, bxx, byy, stan_dev)
    posterior = {}
    for k in likelihood:
        posterior[k] = likelihood[k] * prior
    sum_post = sum(posterior.values())
    posterior = {k: v / sum_post for k, v in posterior.items()}
    direction = max(posterior, key=lambda key: posterior[key])
    print('inferred direction of motion is : {}'.format(direction))

    # Task 3
    stan_dev = 1
    prior = {'up': 1/8, 'down': 5/8, 'left': 1/8, 'right': 1/8}
    likelihood = give_likelihood(rxx, ryy, bxx, byy, stan_dev)
    posterior = {}
    for k in likelihood:
        posterior[k] = likelihood[k]*prior[k]
    sum_post = sum(posterior.values())
    posterior = {k: v / sum_post for k, v in posterior.items()}
    direction = max(posterior, key=lambda key: posterior[key])
    print('inferred direction of motion is : {}'.format(direction))

    # Task 4
    stan_dev = 5
    likelihood = give_likelihood(rxx, ryy, bxx, byy, stan_dev)
    posterior = {}
    for k in likelihood:
        posterior[k] = likelihood[k]*prior[k]
    sum_post = sum(posterior.values())
    posterior = {k: v / sum_post for k, v in posterior.items()}
    direction = max(posterior, key=lambda key: posterior[key])
    print('inferred direction of motion is : {}'.format(direction))


