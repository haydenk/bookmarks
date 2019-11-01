require 'sqlite3'
require 'digest/sha2'

begin
  db = SQLite3::Database.new "bookmarks.db"

  stm = db.prepare "SELECT id, url FROM bookmarks"
  rs = stm.execute

  rs.each do |row|
    id, url = row
    hash = Digest::SHA512.hexdigest(url)
    puts "ID: #{id}"
    puts "URL: #{url}"
    puts "Hash: #{hash}"
    puts
    update_stm = db.prepare"UPDATE bookmarks SET hash_key = ? WHERE id = ?"
    update_stm.execute hash, id
  end

rescue  SQLite3::Exception => error
  puts "Exception occurred"
  puts error
end
