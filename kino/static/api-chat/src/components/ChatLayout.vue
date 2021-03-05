<template>
  <section class="chat-layout">
    <div class="chat-layout-list-container" ref="chatlayout">
      <ul class="chat-layout-list">
        <li class="message"
            v-for="(message, index) in messages"
            :key="index"
            :class="message.author">
          <p>
            <span>
              {{ message.text }}
            </span>
          </p>
        </li>
      </ul>
    </div>
    <div class="chat-inputs">
      <input
          type="text"
          v-model="message"
          @keyup.enter="sendMessage"/>
      <button @click="sendMessage">Send</button>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ChatBox',
  data: () => ({
    message: '',
    messages: []
  }),
  methods: {
    sendMessage() {
      const message = this.message
      this.messages.push({
        text: message,
        author: 'client'
      })
      this.message = ''
      this.$axios.get(`https://www.cleverbot.com/getreply?key=CC8uqcCcSO3VsRFvp5-uW5Nxvow&input=${message}`)
          .then(res => {
            this.messages.push({
              text: res.data.output,
              author: 'server'
            })
            this.$nextTick(() => {
              this.$refs.chatlayout.scrollTop = this.$refs.chatlayout.scrollHeight
            })
          })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.chat-layout,
.chat-layout-list {
  display: flex;
  flex-direction: column;
  list-style-type: none;
}

.chat-layout-list-container {
  height: 36vh;
  overflow-y: scroll;
  margin-bottom: 1px;
}


.chat-layout-list {
  padding-left: 10px;
  padding-right: 10px;

  span {
    padding: 8px;
    color: white;
    border-radius: 4px;
  }

  .server {
    span {
      background: violet;
    }

    p {
      float: left;
    }
  }

  .client {
    span {
      background: blue;
    }

    p {
      float: right;
    }
  }
}

.chat-layout {
  margin: 10px;
  border: 3px solid #39b080;
  width: 20vw;
  height: 40vh;
  border-radius: 3px;
  margin-left: 75%;
  margin-right: auto;
  margin-top: 50vh;
  align-items: normal;
  justify-content: space-between;
}

.chat-inputs {
  display: flex;

  input {
    line-height: 4vh;
    width: 100%;
    border: 1px solid #999;
    border-left: none;
    border-bottom: none;
    border-right: none;
    border-bottom-left-radius: 4px;
    padding-left: 15px;

  }

  button {
    width: 135px;
    color: white;
    background: green;
  }
}
</style>
