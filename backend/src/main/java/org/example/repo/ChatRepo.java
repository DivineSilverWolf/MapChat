package org.example.repo;

import org.example.dao.Chat;
import org.springframework.data.repository.CrudRepository;

public interface ChatRepo extends CrudRepository<Chat, Long> {

}
