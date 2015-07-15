#ifndef _THREADSAFE_QUEUE_
#define _THREADSAFE_QUEUE_

#include <memory> // for shared_ptr


template<class T>
class ThreadSafeQueue {
private:
    std::mutex mut;
    std::queue<T> data_queue;
    std::condition_variable data_cond;

public:
    ThreadSafeQueue();
    ThreadSafeQueue(const ThreadSafeQueue &rhs) {
        std::lock_guard<std::mutex> lg_rhs(rhs.mut);
        // why no lock for myself

        data_queue = rhs.data_queue;
    }

    // disallow assignment for simplicity
    ThreadSafeQueue& operator=(const ThreadSafeQueue &) = delete; 

    void push(T new_entry) {
        std::lock_guard<std::mutex> lg(mut);
        data_queue.push(new_entry);
        data_cond.notify_one();
    }

    // two versions of try pop
    bool tryPop(T& entry) {
        std::lock_guard<std::mutex> lg(mut);
        if (!data_queue.empty()) {
            entry = data_queue.front();
            data_queue.pop();
            return true;
        } else {
            return false;
        }
    }
    std::shared_ptr<T> tryPop() {
        std::lock_guard<std::mutex> lg(mut);
        shared_ptr<T> entry;
        if (!data_queue.empty()) {
            entry = data_queue.front();
        } 
        return entry
    }

    // two versions of pop
    void waitAndPop(T &value) {
        // with unique_lock, it's possible to unlock.
        std::unique_lock<std::mutex> u_lock(mut);

        // lambda function is the condition being waited for.
        // wait() returns if the condition is satisfied.
        data_cond.wait(u_lock, [this](){ return !data_queue.empty(); });
        value = data_queue.front();
        data_queue.pop();
    }
    std::shared_ptr<T> waitAndPop() {

    }

    bool empty() const;
}