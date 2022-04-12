// SPDX-Licence-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // this will get initialized to 0!
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    //People public person = People({favoriteNumber:2, name:"Santi"});

    function store(uint256 _favoriteNumber) public returns(uint256) {
        favoriteNumber = _favoriteNumber;
        return _favoriteNumber;
    }

    //view, pure. Does not make a transaction
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    //memory, data will only be stored during the execution of the function
    //storage data will be stored
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People(_favoriteNumber, _name));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
