import React from "react";
import axios from "axios";
import { TextField, Button, Grid, Box } from "@material-ui/core"
import YouTube from "react-youtube"

class Main extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  async handleSubmit(event) {
    event.preventDefault();
    const response = await axios({
      method: 'post',
      url: '/api/submit',
      data: this.state.value,
      headers: {
        'Content-Type': 'text/plain',
      }
    })
    this.setState({value: ''})
  }

  render() {
    const opts = {
      height: '180',
      width: '320',
      playerVars: {
        // https://developers.google.com/youtube/player_parameters
        autoplay: 1,
      }
    }

    return <main id="mainContent">
      <div className="container">
        <div className="row justify-content-center mt-5 p-0">
          <form onSubmit={this.handleSubmit}>
            <Grid 
              container
              direction="column"
              justify="center"
              alignItems="center"
              spacing={2}
            >
              <Grid item xs={12}>
                Whatever you type in here will be spoken out loud in my room by a robotic voice and displayed on a tiny grid of pixels.
              </Grid>
              <Grid item xs={12}>
                <TextField
                  id="outlined-basic"
                  label="What do you want it to say?"
                  variant="outlined"
                  onChange={this.handleChange}
                  fullWidth
                  inputProps={{ maxLength: 200 }}
                  value={this.state.value}
                />
              </Grid>
              <Grid item>
                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  disabled={!this.state.value.length}
                >
                  Speak
                </Button>
              </Grid>
              <Grid item>
                <Box pt={15}>
                  <YouTube
                    videoId="KADqW056f9k"
                    opts={opts}
                  />
                </Box>
              </Grid>
            </Grid>
          </form>
        </div>
      </div>
    </main>;
  }
}
export default Main;
