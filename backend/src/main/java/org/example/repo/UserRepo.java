package org.example.repo;

import org.example.dao.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepo extends CrudRepository<User, String> { }
