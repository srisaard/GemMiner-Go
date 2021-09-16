package main

import (
	"crypto/rand"
	"flag"
	"fmt"
	"math/big"
	"time"

	"github.com/ethereum/go-ethereum/common"
	solsha3 "github.com/miguelmota/go-solidity-sha3"
)

// no need to change these lines
var chooseFunction = flag.String("callCheckHash", "No", "only check HashRate") // Yes, No
var nonce = flag.Int("nonce", 0, "your nonce")
var diffInt = flag.Int("diff", 10000000000, "difficult now")
var gemKind = flag.Int("kind", 1, "gem kind")
var address = flag.String("address", "0x4E6FEC28f5316C2829D41Bc2187202c70EC75Bc7", "fantom address")
var saltStart = flag.String("salt", "2300000", "salt pointer")

func main() {
	flag.Parse()
	total := int64(0)
	counter := int64(1)
	realNonce := int64(*nonce)
	realDiffInt := int64(*diffInt)
	salt, _ := new(big.Int).SetString(*saltStart, 10)
	// plus := big.NewInt(1)
	realGemKind := int64(*gemKind)
	z := new(big.Int)
	uintMax, _ := z.SetString("115792089237316195423570985008687907853269984665640564039457584007913129639935", 10)
	diff := big.NewInt(realDiffInt)

	var TARGET = new(big.Int).Div(uintMax, diff)
	// fmt.Println("Address:", *address)
	// fmt.Println("Nonce:", realNonce)
	// fmt.Println("Diff:", realDiffInt)
	// fmt.Println("GemKind:", *gemKind)
	start := time.Now().UnixNano()
	for true {
		hash := solsha3.SoliditySHA3(
			// types
			[]string{"uint256", "bytes32", "address", "address", "uint256", "uint256", "uint256"},

			// values
			[]interface{}{
				big.NewInt(250),
				"0x000080440000047163a56455ac4bc6b1f1b88efadf17db76e5c52c0ca594fd9b",
				common.HexToAddress("0x342EbF0A5ceC4404CcFF73a40f9c30288Fc72611"),
				common.HexToAddress(*address),
				big.NewInt(realGemKind),
				big.NewInt(realNonce),
				salt,
			},
		)

		var luck = new(big.Int).SetBytes(hash)
		if *chooseFunction == "No" && luck.Cmp(TARGET) != 1 {
			fmt.Println("FOUND :", salt)
			break
		}

		if counter%100000 == 0 {
			total += counter
			now := time.Now().UnixNano()
			fmt.Println("total hashes", total, "hashes per second : ", total/((now-start)/1e9+1))
			if *chooseFunction == "Yes" {
				break
			}
			start := time.Now().UnixNano()
			_ = start
			counter = 1
		}

		// salt.Add(salt, plus)
		salt, _ = rand.Int(rand.Reader, uintMax)
		// fmt.Println("Current :", salt)
		counter += 1
	}
}
