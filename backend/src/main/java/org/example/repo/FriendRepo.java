package org.example.repo;

import org.example.dao.Friend;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface FriendRepo extends CrudRepository<Friend, Long> {
//   @Query("select Friend.id from Friend where Friend.username == :username and Friend.friend == :friend");
//   Long getIdByFriend(String username, String friend);
}
